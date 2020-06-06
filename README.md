# Simple Sundanese Translator
Simple Sundanese to Bahasa Indonesia translator using Pattern Matching (only implemented by per-word matching) . Back-end created with Flask and Python, and front-end using vanilla HTML and CSS that rendered with jinja2.

## Requirements
-----------
1. *Python 3*, here I'm using python 3.7
2. Recommended using *Windows*, as I'm using it. But, you can try in linux, such as Ubuntu Linux
3. Latest Web Browser, recommended using *Google Chrome* or *Mozilla Firefox* as I've tested this web apps work on them.
4. *Virtualenv* (a python lib, for creating virtual/special environment to a specific project)
5. Additional python lib/framework: *flask*, *python-dotenv* (of course all of it installed in venv)
   
You can install virtualenv by executing **install_venv.bat**, and when inside virtuelenv, you can executing **install_library.bat** to install additional python library needed for this web application.

## How to Run
------------
1. Make sure you've install all requirements above. If you don't, please follow step that I've mentioned above (for some requirements) before you proceed to the next step.
2. open shell (cmd/powershell) and change directory to **env/Script**.
3. Execute
    
            activate
    to run virtualenv.
4. Execute
      
        flask run
   to run the server.

For simplicity you can executing **start_env.bat** instead of step 2-3 to running virtualenv for simplicity.

## How to Use
--------
1. After you run the server by *flask run*, you can navigate to 
   
        http://127.0.0.1:5000/
   or

        localhost:5000/

   with your web browser to run this web apps. 
2. Choose the mode (indo to sunda / sunda to indo), the algorithm that should be used, input the text that want to be translated, and then click **Translate** button.
3. The translation must appear after awhile.
4. Enjoy.

## Sample Input and Output of the Translation
```
Sunda - Indonesia
Sunda : nami abdi Riyugan
Indonesia : nama saya Riyugan
```

```
Sunda - Indonesia
Sunda : abdi teh sanes jalma Bandung
Indonesia : saya bukan orang Bandung
```

```
Sunda - Indonesia
Sunda : anjeun sumping ti mana?
Indonesia : kamu tiba dari mana?
```

```
Indonesia - Sunda
Indonesia : nama saya Riyugan
Sunda : nami abdi Riyugan
```

```
Indonesia - Sunda
Indonesia : nama adik kamu siapa?
Sunda : nami rai anjeun teh saha?
```

```
Indonesia - Sunda
Indonesia : saya tidak bisa bahasa Sunda
Sunda : abdi henteu tiasa bahasa Sunda
```

## Known Bugs or Problems
1. The Indentation in textarea (input/ output text section) after translation would give *tab* before the translation, but the translation result should be correct.

## Documentation
You can access how to use this program in (this youtube)[] link.
