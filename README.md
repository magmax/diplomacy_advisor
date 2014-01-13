# WebDiplomacy alert

We really like [webdiplomacy], but it has no email alerts. So here you are the solution!


## How to use it

You need a **advisor.cfg** file. The file *advisor.cfg.sample* is provided as example.

Here you can configure your game, your email preferences and map each country with the email to be alerted. So easy!

Remember to change the game id!!!

You can add it to your **cron** daemon and execute it periodically. For example, each two hours:

    0 */2 * * * cd /path/to/diplomacy/alert && ./advisor.py > /dev/null


## License

The MIT License (MIT)

Copyright (c) 2014 Miguel Angel Garcia<miguelangel.garcia@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


[webdiplomacy]: http://webdiplomacy.net/index.php