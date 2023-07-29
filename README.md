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
* Backend: **Python Fast-API, concurrent.futures (For Parallelizing Scrape), xvfbwrapper** 
* Web Scraping: **Playwright, requests, BeautifulSoup4, urllib, googlesearch, pandas, numpy**
* Frontend: **React JS, HTML, CSS**
* ![React][React.js]
[React.js]: https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=React&logoColor=white

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
