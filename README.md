# Crack-CAPTCHA
My Record for CAPTCHA Cracking!!!!

## Content:
- [Weibo Click CAPTCHA (geetest)](#click-captcha)

## Click CAPTCHA
When you use some weibo account to [login weibo.cn](https://passport.weibo.cn/signin/login
), sometimes you'll meet this CAPTCHA(Usually when you have a remote login):

<div align=center><img width="400" height="300" src="https://raw.githubusercontent.com/RunningIkkyu/Crack-CAPTCHA/master/img/bg.PNG"/></div>



</br>And you can see the effect:</br></br>



![Cracking Demo](https://raw.githubusercontent.com/RunningIkkyu/Crack-CAPTCHA/master/img/GIF.gif)

### Pre-requirements

- Install requirements.txt
- Install Chrome
- Install ChromeDriver
- Unpackage ChromeDriver and add it to your PATH


Before using this program to crack CATCHA, It's assumed you have install python(>3.5) in your system.</br>
These package will be reqired:
selenium==3.141.0
pymongo==3.7.2
PyAutoGUI==0.9.41

You can install requirements by this:

```
pip install -r requirements.txt
```

also you need a Chrome and ChromeDriver:</br>

You can get Chromedriver from [here](http://chromedriver.storage.googleapis.com/index.html).

**Make sure the version of Chrome Driver is matched with your Chrome.**

After download Webdriver, remember add it to path. If you're using Linux, run this:

```
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```
