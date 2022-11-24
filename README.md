<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/aglorenz/Download-Repo">
    <img src="images/DRU-Logo_transparent.png" alt="Logo" width=110" height="110">
  </a>

  <h1>Download Repository Utility</h1>

                                                                                 
  <p>
    A utility to quickly download a GitHub repository, unzip it, and open the top-level folder in file explorer.
    <br />
    <a href="https://github.com/aglorenz/Download-Repository-Utility"><strong>Explore the docs »</strong></a>
    <br />
    <br />
<!--    <a href="https://github.com/aglorenz/Download-Repository-Utility">View Demo</a>
    · -->
    <a href="https://github.com/aglorenz/Download-Repository-Utility/issues">Report Bug</a>
    ·
    <a href="https://github.com/aglorenz/Download-Repository-Utility/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#quick-start">Quick Start</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
      <ul>
        <li><a href="#enter-repo-url-input-field">"Enter Repo URL"Input Field</a></li>
        <li><a href="#mainmaster-radio-button">"Main/Master" Radio Button</a></li>
        <li><a href="#other-radio-button">"Other" Radio Button</a></li>
        <li><a href="#browse-dest-input-field-and-button">"Browse Dest" Input Field and Button</a></li>
        <li><a href="#download-repo-button">"Download Repo" Button</a></li>
        <li><a href="#output-text-box">"Output" Text Box</a></li>
        <li><a href="#drulog">DRU.log</a></li>
        <li><a href="#housecleaning">Housecleaning</a></li>
      </ul>
    <li><a href="#limitations-and-exceptions">Limitations and Exceptions</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![DRU Screenshot](https://user-images.githubusercontent.com/27447653/198150984-a841f3f6-fcb3-4beb-8f78-99d9a03e15fa.png)

As instructors at a software development boot camp, we download between 70 and 100 GitHub student repositories a day.  The process to download a repository and open the assignment folder is monotonous and takes up to 20 mouse/key clicks.  In a fast paced environment with frequent interruptions, it's easy to lose your place and have to repeat steps or start over :expressionless:. As a fan of efficient work flow, I was inspired to create Download Repository Utility (DRU). Once it's up and runnning, DRU only takes 2 or 3 clicks to download a repo, open the student folder, and begin code review. Just paste the URL and press Enter :sunglasses:.  Almost everything is automated including opening the repository folder and deleting the zip file.

### Features
- Fast download (using Powershell 5.1 and Web Client) and fast reliable unzip (using 7-zip).
- Repository folder is auto-opened in Windows File Explorer so you can get to work quickly.
- Zip file is deleted after unzip.
- Delayed tooltips when mouse is hovered over GUI features.
- Remembers specified download destination for next run.
- Unzipped repository folder is prefixed with the username to make it unique. This prevents unzipping into another student's folder that has the same repo name.
- Can specify branch to download if repo contains multiple branches.
- Important information and errors are displayed on screen, more details are written to DRU.log.
- Screen size is flexible.  Just click and drag borders to adjust the footprint.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python-shield]][Python-url]
* [![Tkinter][Tkdocs-shield]][Tkinter-url]
* [![Powershell][Powershell-shield]][Powershell-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Getting Started -->
## Getting Started

To get a local copy up and running follow these steps:

### Prerequisites

DRU was developed and tested with the following:
* Windows 10 or 11
* Python 3.9.5
* PowerShell 5.1 (comes installed with Windows 10 and 11)
* Python libraries
    * Pyglet 1.5.27
    * Pillow 9.3.0

To install Python:
* [Python download](https://www.python.org/downloads) (latest version is OK)

To install the Python libraries:
(Use a python virtual environment if your main python environment has different versions of below libraries)
* After installing Python, open the Windows command line and execute the following:
  ```sh
  pip install pyglet==1.5.27  (pyglet 2.0 will not load our cool external computer font 🙁)
  pip install Pillow==9.3.0
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/aglorenz/Download-Repository-Utility.git
   ```
2. Ensure the prerequisites above have been met.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Quick Start

1. Navigate to the main folder of the repository, "Download-Repository-Utility".
2. Open DRU.py with [IDLE](https://docs.python.org/3/library/idle.html).
3. Click Run ➡️ Run Module to open DRU.
4. Copy and paste a GitHub repository URL into the "Enter Repo URL" field and press **enter** on your keyboard to begin the repo download and extraction.
<p align="right">(<a href="#readme-top">back to top</a>)</p>
                                       
#### Generate a Shortcut for the Taskbar

1. Right click on DRU.py ➡️ Properties
2. In the **Target** field:
    * Enter the path to your python.exe file. **Note:** The path on your machine may differ significantly.  
       Ex: **C:\Users\Andy\AppData\Local\Programs\Python\Python39\python.exe**  
       If your path has a space in one of the folder names, surround the whole path with double (not single) quotes like so:  
       **"C:\Users\Andy\AppData\Local\Programs\Python\Python39\python.exe"**  
    * Change python.exe to **pythonw**.exe
    * Add a space and paste the path to the DRU.py file location.
    * The finished **Target** field should look like so:  
       **C:\Users\Andy\AppData\Local\Programs\Python\Python39\pythonw.exe C:\Users\Andy\Source\Repos\Download-Repository-Utility\DRU.py**
2. In the **Start In** field
    *  Enter the path to DRU.py Ex: **C:\Users\Andy\Source\Repos\Download-Repository-Utility**
3. Click Apply
4. Click Change Icon... ➡️ Browse
    * Browse to the Images subfolder of the repository and select DRU-Favicon-Thick.ico ➡️ Open ➡️ OK ➡️ OK
5. Drag the shortcut to the taskbar

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE -->
## Usage

### "Enter Repo URL" Input Field
Paste a repository URL into this field.  The URL must contain the **https://** prefix and at least a valid GitHub **username** and **repository** name.
  ```
  Ex:  https://github.com/JoeSchmo/JavaScript-Projects/...
  ```
* For the fastest workflow, press the **enter** key after pasting the URL to begin the download process.  
* After the repository is downloaded and unzipped, the folder name is prefixed with the GitHub user's name to differentiate it from other repositories with the same name.
* Once the repository is unzipped, the folder is auto-opened in Windows File Explorer

### "Main/Master" Radio Button
* If the repo contains either a Main or Master branch (but not both) select **Main/Master**.  
* If the repo contains both branches and content from Master is needed, select **Main/Master**.
* If the repo contains both branches and content from Main is needed, select **Other** and enter **main** in the input field. 

### "Other" Radio Button
* Select this if content from an alternative branch (which could be **main**) is needed. Enter this branch name in the input field.

### "Browse Dest" Input Field and Button                                                                  
* If a custom destination is desired for the downloaded repositories, enter the path in the input field or press the button to open a browse dialog to select a folder.  If this field is left blank, DRU will use "C:/temp".  If this folder doesn't exit, it will be auto-created.
* The path entered will be saved in DRU.ini and repopulated the next time DRU is opened.

### "Download Repo" Button                                                                   
* To start the download, click this button as an alternative to pressing **enter** after entering the repo URL.

### "Output" Text Box
* Informative output from DRU is displayed here including:
  * Most recently used repo URL
  * User, Repository Name, Branch Name
  * Error messages
* Output text box can be resized by dragging the borders of the DRU application GUI.
* Output content can be scrolled by hovering the mouse and scrolling the wheel.

### DRU.log
* This file contains behind-the-scenes details from the last download to help with debugging.

### Housecleaning
* User will need to: 
  * Manually close the File Explorer Window after they are done with it.
  * Manually delete the unzipped folder when they are done with it (zip files are auto-deleted).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Limitations and Exceptions -->
## Limitations and Exceptions
                                       
* DRU cannot: 
  * Download a repository that ends with a period.  These must be downloaded manually from GitHub. It's a limitation of Web Connect.
  * Display a download progress bar. It only displays 100% once the download is complete to give the feeling of progress. There are code examples online that can download a repository and show a progress bar, but they take 4X longer.  Web Connect used here is much faster.  In this case download speed was more important than usablility.  

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Modified Tkinter ToolTips library to accept a custom function. This allowed button color change on mouse hover followed by a delayed tooltip.
- [ ] Package DRU as an executable.
- [ ] Better looking delayed tooltips with customizable color, font, and border.

See the [open issues](https://github.com/aglorenz/Download-Repository-Utility/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Andrew Lorenz : [LinkedIn](https://www.linkedin.com/in/andrew-lorenz-565208133/)

Project Link : [https://github.com/aglorenz/Download-Repository-Utility](https://github.com/aglorenz/Download-Repository-Utility)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Alex Sanderson](https://github.com/Vexelior) : For pointing me toward the more efficient Web Connect.
* [Wesley Morford](https://github.com/WMorf) : Alpha Testing.
* [An Awesome README template](https://github.com/othneildrew/Best-README-Template)
* [Choose an Open Source License](https://choosealicense.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/aglorenz/download-repository-utility.svg?style=for-the-badge
[contributors-url]: https://github.com/aglorenz/download-repository-utility/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/aglorenz/download-repository-utility.svg?style=for-the-badge
[forks-url]: https://github.com/aglorenz/download-repository-utility/network/members
[stars-shield]: https://img.shields.io/github/stars/aglorenz/download-repository-utility.svg?style=for-the-badge
[stars-url]: https://github.com/aglorenz/download-repository-utility/stargazers
[issues-shield]: https://img.shields.io/github/issues/aglorenz/download-repository-utility.svg?style=for-the-badge
[issues-url]: https://github.com/aglorenz/download-repository-utility/issues
[license-shield]: https://img.shields.io/github/license/aglorenz/Download-Repository-Utility.svg?style=for-the-badge
[license-url]: https://github.com/aglorenz/Download-Repository-Utility/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/andrew-lorenz-565208133
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Django-shield]: https://img.shields.io/badge/django-092d1f?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://djangoproject.com
[Tkdocs-shield]: https://img.shields.io/badge/Tkinter-3772a4?style=for-the-badge&logo=python&logoColor=ffd13f
[Tkinter-url]: https://tkdocs.com
[Python-shield]: https://img.shields.io/badge/Python-3674a8?style=for-the-badge&logo=python&logoColor=ffd13f
[Python-url]: https://python.org
[Powershell-shield]: https://img.shields.io/badge/Powershell-03438e?style=for-the-badge&logo=powershell&logoColor=a4d2e8
[Powershell-url]: https://learn.microsoft.com/en-us/powershell/
