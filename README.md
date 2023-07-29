# Food-Price-Clash 
Compare the Best Food before Order

### Swiggy vs Zomato Real Time Price Comparison Website
> * This Web App Compares Price Between  _Swiggy_ and _Zomato_ by Real Time (live) Web Scraping and Data Analysis.
> * Within few Clicks User can see the Exclusive Food Name + Prices in Result Table from particular Restuarants from _Swiggy_ and _Zomato_ websites.
> * After Analysis User will get direct Suggestion - "Which Food Delivery site is cheaper?".
> * Also User can see cheaper Food Item on Result Table in _Green_ colour.

Check out Complete Demo
[![Video Title](https://img.youtube.com/vi/C5kNgWme1zs/0.jpg)]([https://www.youtube.com/watch?v=VIDEO_ID](https://www.youtube.com/watch?v=C5kNgWme1zs))

#### Tech Stacks:
* Backend: **Python Fast-API, concurrent.futures (For Parallelizing Scrape), xvfbwrapper** 
* Web Scraping: **Playwright, requests, BeautifulSoup4, urllib, googlesearch, pandas, numpy**
* Frontend: **React JS, HTML, CSS**

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
