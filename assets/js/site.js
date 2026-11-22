(() => {
  const gallery = document.querySelector('.hero-gallery');
  if (gallery) {
    const hero = document.querySelector('.hero');
    const coarse = matchMedia('(pointer: coarse)');
    const reduced = matchMedia('(prefers-reduced-motion: reduce)');
    let scheduled = false, target = 0;
    const position=document.querySelector("[data-gallery-index]");
    const move = () => { gallery.scrollLeft = target * (gallery.scrollWidth-gallery.clientWidth); scheduled=false;
      if(position)position.textContent=String(Math.round(target*(gallery.children.length-1))+1).padStart(2,"0")+" / "+String(gallery.children.length).padStart(2,"0"); };
    const queue = (x) => { target=Math.max(0,Math.min(1,x)); if(!scheduled){scheduled=true;requestAnimationFrame(move);} };
    hero.addEventListener('pointermove', e => {
      if(coarse.matches || reduced.matches || e.target.closest('a,button')) return;
      const r=hero.getBoundingClientRect(); queue((e.clientX-r.left)/r.width);
    }, {passive:true});
    // Preserve mobile vertical-scroll-to-gallery interaction without taking over scrolling.
    window.addEventListener('scroll',()=>{
      if(!coarse.matches || reduced.matches) return;
      const r=hero.getBoundingClientRect(); if(r.bottom>0 && r.top<=0) queue(-r.top/r.height);
    },{passive:true});
    document.querySelectorAll('[data-gallery-step]').forEach(button=>button.addEventListener('click',()=>{
      const count=gallery.children.length;
      const index=Math.round(gallery.scrollLeft/gallery.clientWidth);
      target=((index+Number(button.dataset.galleryStep)+count)%count)/(count-1); move();
    }));
  }
  const ui=window.NF_UI||{};
  const mainlandChoices = document.querySelectorAll('template[data-mainland-download]');
  if (mainlandChoices.length) {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 5000);
    fetch('https://api.country.is/', {
      signal: controller.signal, credentials: 'omit', referrerPolicy: 'no-referrer', cache: 'no-store'
    }).then(async response => {
      if (!response.ok || (await response.json()).country !== 'CN') return;
      for (const choice of mainlandChoices) {
        choice.previousElementSibling.replaceWith(choice.content.cloneNode(true));
        choice.remove();
      }
      const copyButton = document.querySelector('[data-copy-code]');
      if (copyButton) copyButton.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText('55b5');
          copyButton.textContent = ui.copied;
        } catch {
          copyButton.textContent = ui.copyFail;
        }
      });
    }).catch(() => {
      // Keep the default App Store link when the region is unavailable.
    }).finally(() => clearTimeout(timeout));
  }
  const navDetails=document.querySelector('.guide-sidebar details');
  if(navDetails){const wide=matchMedia('(min-width: 701px)');navDetails.open=wide.matches;wide.addEventListener('change',e=>{navDetails.open=e.matches;});}
  const search=document.querySelector('.doc-search'), results=document.querySelector('.search-results');
  if(search && window.NF_SEARCH){
    search.addEventListener('input',()=>{
      const q=search.value.trim().toLocaleLowerCase();results.replaceChildren();
      if(!q) return;
      const terms=q.split(/\s+/);
      const matches=NF_SEARCH.filter(x=>terms.every(t=>(x.title+' '+x.text).toLocaleLowerCase().includes(t))).slice(0,8);
      if(!matches.length){results.textContent=ui.searchEmpty||'没有找到相关内容，试试“裁切”“Dmin”或“快捷键”。';return;}
      for(const item of matches){const a=document.createElement('a');a.href=item.slug+'.html';a.textContent=item.title;const small=document.createElement('small');small.textContent=item.description;a.append(small);results.append(a);}
    });
  }
  const slidesButton = document.querySelector('.workspace-slides');
  if (slidesButton) {
    const slides = Array.from(slidesButton.children);
    const counter = slidesButton.parentElement.querySelector('.workspace-count span');
    const playback = slidesButton.parentElement.querySelector('.workspace-playback');
    const motion = matchMedia('(prefers-reduced-motion: reduce)');
    let playing = !motion.matches;
    let visible = false;
    let current = 0, requested = 0, timer;

    function prepare(index) {
      const slot = slides[index];
      if (slot.tagName === 'TEMPLATE') {
        const image = slot.content.querySelector('img');
        image.loading = 'eager';
        image.setAttribute('aria-hidden', 'true');
        slot.replaceWith(image);
        slides[index] = image;
      }
      return slides[index];
    }

    function schedule() {
      clearTimeout(timer);
      if (!playing || !visible || document.hidden || requested !== current) return;
      if (!slides[current].complete || !slides[current].naturalWidth) return;
      prepare((current + 1) % slides.length);
      timer = setTimeout(next, 3000);
    }

    async function next() {
      clearTimeout(timer);
      const index = (requested + 1) % slides.length;
      requested = index;
      const image = prepare(index);
      try {
        await image.decode();
      } catch {
        if (requested === index) { requested = current; schedule(); }
        return;
      }
      if (requested !== index) return;
      if (index !== current) {
        slidesButton.querySelector('.previous')?.classList.remove('previous');
        slides[current].className = 'previous';
        slides[current].setAttribute('aria-hidden', 'true');
        // Commit the incoming frame's initial opacity before starting the fade.
        image.getBoundingClientRect();
        image.className = 'current';
        image.removeAttribute('aria-hidden');
        current = index;
        counter.textContent = String(current + 1).padStart(2, '0');
      }
      schedule();
    }

    function setPlaying(value) {
      playing = value;
      playback.textContent = playing ? 'Ⅱ' : '▶';
      playback.setAttribute('aria-label', playing ? playback.dataset.pause : playback.dataset.play);
      schedule();
    }
    slidesButton.addEventListener('click', next);
    playback.addEventListener('click', () => setPlaying(!playing));
    playback.hidden = false;
    setPlaying(playing);
    motion.addEventListener('change', () => setPlaying(!motion.matches));
    slides[0].addEventListener('load', schedule, { once: true });
    document.addEventListener('visibilitychange', schedule);
    new IntersectionObserver(([entry]) => {
      visible = entry.isIntersecting;
      schedule();
    }).observe(slidesButton);
  }
  const images=document.querySelectorAll('.prose img');
  if(images.length){
    const dialog=document.createElement('dialog');dialog.className='lightbox';dialog.setAttribute('aria-label',ui.lightbox||'查看大图');
    const close=document.createElement('button');close.textContent=ui.close||'关闭 ×';const preview=document.createElement('img');dialog.append(close,preview);document.body.append(dialog);
    close.addEventListener('click',()=>dialog.close());dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close();});
    for(const img of images){const a=document.createElement('a');a.href=img.src;a.className='image-link';a.setAttribute('aria-label',(ui.zoom||'放大：')+img.alt);img.before(a);a.append(img);img.dataset.zoom='';a.addEventListener('click',e=>{if(typeof dialog.showModal!=='function')return;e.preventDefault();preview.src=img.src;preview.alt=img.alt;dialog.showModal();});}
  }
})();
