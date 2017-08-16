Title: Using Pelican for Blogging
Date: 2017-08-15 12:05
Category: Python
Tags: python, tutorial
Slug: PelicanForBlogging
Author: Gustavo Sandoval
Summary: Using Pelican as a static Blogging Platform


#Using Pelican for my new Blog#

I finally decided to spend the time to do all the plumbing to have my own blog.

I didn't use [Medium](<http://medium.com>), [WordPress](http://wordpress.com) or [Blogger](<http://www.blogger.com>) because:
1.  I needed to have [iPython](<http://ipython.com>) notebooks inline without having to convert them to html or PDF.
2.  I wanted to deploy my blog using github pages
3.  I didn't want to depend on a database


So after reading about some different options I decided to go with [Pelican](http://docs.getpelican.com/) because it has a lot of support in terms of plugin and themes. Also because it's written in Python which I'm more confortable with than Ruby.

After making the decision to go with Pelican I used the following blogs for reference while still having to experiment with a few things.  I am writing this to document what worked and what didn't.

Sites that helped me:

1. [Pythonic Perambulations](<https://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/>)

2. [Fedora Magazine](<https://fedoramagazine.org/make-github-pages-blog-with-pelican/>)

3. [Notions and Notes](http://www.notionsandnotes.org/tech/web-development/pelican-static-blog-setup.html)

These are some notes on what worked for me:

	* Create two github repos: gussand.github.io and gussand.github.io-src

	* Create a new virtualenv for python for your blog because chance are that the one you have won't work with embedding iPython notebooks


The mechanics:

To create a new entry:

	- save it in the content directory.

	- type: make html & make serve

to commit and publish it's a little more complicated.

What was written in some blogs about making your output directory username.github.io didn't work because the git
folder got overwritten. What worked for me was using ghp-import.

Here are the commands:

	*   pelican content -o output -s pelicanconf.py
  	*   ghp-import output
  	*   git push git@github.com:gussand/gussand.github.io.git gh-pages:master
