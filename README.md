# youtubedl-gui

## Description
  This application was designed to provide a lightweight and easy to use GUI for [youtube-dl](https://github.com/ytdl-org/youtube-dl), a command line library used to get videos from YouTube. 
  
  Throughout the internet, there are plenty examples of shady websites and applications that claim to quickly gather the mp3/mp4 file for a YouTube link, but are typically littered with ads and false download links. Instead of having to go through the process of dodging downloads and putting on an ad blocker, or rely on a service that may not exist soon, we thought it would be easier to have a simple desktop application to quickly gather needed videos without having to rely on external hardware.
  
  While youtube-dl is a great command-line application, we found that more casual desktop users do not find command line interfaces as friendly, so we found that a lightweight implementation of [PySimpleGUI](https://www.pysimplegui.org/en/latest/) as well as tkinter and the other libraries for creating simple GUI's in Python had a much better UI/UX than the shady websites mentioned before.


## Instructions
  To run this program, ensure the latest version of Python is installed, and run from the command line.
  
  A GUI will open. Enter the directory in which you want your video to be saved, as well as the link that you want to download, and click download, and the video will be downloading.


## Credits, Contributions
  ### Authors
  Organizing Developer - Evann M Hall
  
  Lead Developer/UI Developer - Tyler J Heinz
  
  Developer - Chandler J Horton
  
  Thank you to all that have been involved and contributed.
  
  ### External Dependencies

  [youtube-dl](https://github.com/ytdl-org/youtube-dl)
  
  [PySimpleGUI](https://www.pysimplegui.org/en/latest/)

## Suggestions
  Direct any suggestions, changes, bug reports, etc. to https://github.com/halle15/youtubedl-gui/issues

## License
  Usage, distribution, modification and etc. fall under the Universal Permissive License v1.0
  
  Copyright (c) 2020 Tyler J Heinz, Chandler J Horton, Evann M Hall

The Universal Permissive License (UPL), Version 1.0

Subject to the condition set forth below, permission is hereby granted to any
person obtaining a copy of this software, associated documentation and/or data
(collectively the "Software"), free of charge and under any and all copyright
rights in the Software, and any and all patent rights owned or freely
licensable by each licensor hereunder covering either (i) the unmodified
Software as contributed to or provided by such licensor, or (ii) the Larger
Works (as defined below), to deal in both

(a) the Software, and
(b) any piece of software and/or hardware listed in the lrgrwrks.txt file if
one is included with the Software (each a “Larger Work” to which the Software
is contributed by such licensors),

without restriction, including without limitation the rights to copy, create
derivative works of, display, perform, and distribute the Software and make,
use, sell, offer for sale, import, export, have made, and have sold the
Software and the Larger Work(s), and to sublicense the foregoing rights on
either these or other terms.

This license is subject to the following condition:
The above copyright notice and either this complete permission notice or at
a minimum a reference to the UPL must be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
