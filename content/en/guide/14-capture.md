# File formats and tethered capture

NextFrame can process camera copies and scans. It can also connect to a supported camera, or watch a capture folder.

## Import files

In the library, click Import Folder, or drop a folder onto the library area. Use Add Frames for one file or several.

Common inputs are camera RAW (for example ARW, NEF, CR2/CR3, and RAF), DNG, TIFF, and FFF. Whether a specific camera and encoding can be read is decided by the import result. Choose the single-copy path or the strip path to match the film.

Before import, check the source color space for DNG and TIFF, and the camera DCP settings, in Processing Preferences. They should match the source file. TIFF files from different scan software do not always use the same color space.

## Connect a camera

1. Connect the camera with a cable, turn it on, and choose a connection mode that allows computer control.
2. In the NextFrame library, click Tethered Capture.
3. Click Connect and choose a detected, supported device.
4. Check live view. Where the controls are available, set exposure mode, shutter, ISO, white balance, quality, and size.
5. Click the shutter button. After the photo transfers, it enters the current workflow. If import auto-processing is on, processing continues from your preferences.
6. Disconnect when you are done.

Available controls depend on the camera and the connection. Set anything the computer cannot change on the camera body. If live view is unavailable, turn it on from the camera when the interface says so, or just take the picture. If a device cannot release the shutter remotely, use the shutter on the body.

## Watch a folder

If you already have camera-control software, let it save photos to a local folder and let NextFrame pick up new files.

1. Import that folder into NextFrame and select it.
2. Open Tethered Capture and click Watch Folder. The current library item needs a real path on disk, and no camera should be connected.
3. In the camera software, set the save location to the same folder.
4. After a shot, wait for the file to finish writing, then look at the new photo and its processing result in NextFrame.
5. Use Pause, Resume, or Close on the floating status bar to control watching.

Shoot one test file first. Confirm the save location, format, and automatic processing, then shoot the rest of the roll.
