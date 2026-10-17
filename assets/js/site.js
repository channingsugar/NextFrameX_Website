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
  document.querySelectorAll('[data-copy-code]').forEach(button=>button.addEventListener('click',async()=>{
    try{await navigator.clipboard.writeText('55b5');button.textContent=ui.copied||'已复制';}
    catch{button.textContent=ui.copyFail||'提取码：55b5';}
  }));
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
  const images=document.querySelectorAll('.prose img,.overview-image img');
  if(images.length){
    const dialog=document.createElement('dialog');dialog.className='lightbox';dialog.setAttribute('aria-label',ui.lightbox||'查看大图');
    const close=document.createElement('button');close.textContent=ui.close||'关闭 ×';const preview=document.createElement('img');dialog.append(close,preview);document.body.append(dialog);
    close.addEventListener('click',()=>dialog.close());dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close();});
    for(const img of images){const a=document.createElement('a');a.href=img.src;a.className='image-link';a.setAttribute('aria-label',(ui.zoom||'放大：')+img.alt);img.before(a);a.append(img);img.dataset.zoom='';a.addEventListener('click',e=>{if(typeof dialog.showModal!=='function')return;e.preventDefault();preview.src=img.src;preview.alt=img.alt;dialog.showModal();});}
  }
})();
