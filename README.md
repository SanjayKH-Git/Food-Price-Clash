# Food-Price-Clash 
Compare the Best Food before Order

### Swiggy vs Zomato Real Time Price Comparison Website
> - [X] This Web App Compares Price Between  _Swiggy_ and _Zomato_ by Real Time (live) Web Scraping and Data Analysis.
> - [X] Within few Clicks User can see the Exclusive Food Name + Prices in Result Table from particular Restuarants of _Swiggy_ and _Zomato_ websites.
> - [X] User will get direct Suggestion - **"Which Food Delivery site is cheaper?"** from Price-Analysis
> - [X] Also User can see **cheaper Food Item** on Result Table in _Green_ colour.

#### Check out Complete Demo
[![Video Title](https://img.youtube.com/vi/C5kNgWme1zs/0.jpg)]([https://www.youtube.com/watch?v=VIDEO_ID](https://www.youtube.com/watch?v=C5kNgWme1zs))

#### Tech Stacks:
* Backend: ![Python][Python] ![FastAPI][FastAPI]
  > ![concurrent.futures][concurrent.futures]
  > ![xvfbwrapper][xvfbwrapper]
  > 
[Python]: https://img.shields.io/badge/-Python-07065c?style=flat-square&logo=python&logoColor=white
[FastAPI]: https://img.shields.io/badge/-FastAPI-22293E?style=flat-square&logo=fastapi&logoColor=white
[concurrent.futures]: https://img.shields.io/badge/-concurrent.futures-6772E5?style=plastic&logo=python&logoColor=white
[xvfbwrapper]: https://img.shields.io/badge/-xvfbwrapper-8856D0?style=plastic&logo=xvfbwrapper&logoColor=white

* Web Scraping:
  > ![Playwright][Playwright]
  > ![requests][requests]
  > ![BeautifulSoup4][BeautifulSoup4]
  > ![urllib][urllib]
  > ![Googlesearch][Googlesearch]
  > ![Pandas][Pandas]
  > ![Numpy][Numpy]

* Frontend:
  > ![React][React.js]
  > ![HTML][HTML]
  > ![CSS][CSS.js]
  
[Playwright]: https://img.shields.io/badge/-Playwright-408f04?style=plastic&logo=playwright&logoColor=white
[requests]: https://img.shields.io/badge/-requests-ad078f?style=plastic&logo=requests&logoColor=white
[BeautifulSoup4]: https://img.shields.io/badge/-BeautifulSoup4-0097A7?style=plastic&logo=beautifulsoup4&logoColor=white
[urllib]: https://img.shields.io/badge/-urllib-CC3333?style=plastic&logo=urllib&logoColor=white
[Googlesearch]: https://img.shields.io/badge/-Googlesearch-4285F4?style=plastic&logo=googlesearch&logoColor=white
[Pandas]: https://img.shields.io/badge/-Pandas-177171?style=plastic&logo=pandas&logoColor=white
[Numpy]: https://img.shields.io/badge/-Numpy-0072BD?style=plastic&logo=numpy&logoColor=white
[React.js]: https://img.shields.io/badge/-React-6d0f87?style=flat-square&logo=React&logoColor=white
[HTML]: https://img.shields.io/badge/-HTML-E34F26?style=flat-square&logo=html5&logoColor=white
[CSS.js]: https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white

## **Running Application in _Codespace_**
create env 
```shell
virtualenv env
```
Activate env
```shell
source env/bin/activate
```
Split _terminal_ into 2 parts **( Left for Backend & Right for frontend )**
```cpp
ctrl + shift + 5 or cmd + shift + 5
```
Run Fast API Backend _(Left)_
```shell
uvicorn main:app --reload
```
 Run React JS Frontend _(Right)_
```shell
cd frontend
npm start
```
