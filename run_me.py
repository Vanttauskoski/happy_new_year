#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
__author__ = 'nullexception'
import sys
import time
import sys
from power_console import *
import random

date = u"""
★░★░★░★░▀▀▀▀█░░█▀▀▀█░░▀█░░█░░░█░★░★░★░★ 
★░★░★░★░█▀▀▀▀░░█░░░█░░░█░░▀▀▀▀█░★░★░★░★ 
★░★░★░★░▀▀▀▀▀░░▀▀▀▀▀░░░▀░░░░░░▀░★░★░★░★"""

lable_linux = u"""
✷░░░█▀▀░░█░█░█▀█░█▀█░░█░░░█░█▀▌░▐▀█░░░✷
❂░░░█░░░░█▀█░█░█░█▀▀█░█▀█░█░█░▀█▀░█░░░❂
✹░░░▀▀▀░░▀░▀░▀▀▀░▀▀▀▀░▀▀▀░▀░▀░░▀░░▀░░░✹
✶░░░░░░█▀▀░█▀█░░█▀█░░█▀█░█▀▌░▐▀█░░░░░░✶
✳░░░░░░█░░░█░█░░█░█░░█░█░█░▀█▀░█░░░░░░✳
✸░░░░░░▀░░░▀▀▀░▐▀▀▀▌░▀▀▀░▀░░▀░░▀░░░░░░✸
"""

text = """
Дорогие друзья! Поздравляю вас с новым 2014 годом!
Желаю всем вам в наступающем году много новых и интересных задач!
Чтобы количество начатых проектов равнялось количеству успешных релизов!
Также желаю вам, чтобы вы реже встречались с синьором Dead_Line-ом!
Дорогие друзья, желаю вам чаще покидать околокомпьютерное-диванное пространство и 
проводить время вместе с друзьями, любимыми и близкими вам людьми 
(поверьте, им вас не хватает).
"""

star_linux = u"""           ★\n"""

tree_head_linux = u"""           █"""

tree_1_linux = u"""          █▓█
         █▓▓▓█
        █▓▓▓▓▓█
       █▓▓▓▓▓▓▓█
      █▓▓▓▓▓▓▓▓▓█
     █▓▓▓▓▓▓▓▓▓▓▓█
    █▓▓▓▓▓▓▓▓▓▓▓▓▓█
   █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
 █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"""

tree_trunk_linux = u"""           ██
           ██"""

star_windows = """
           *"""

tree_head_windows = u"""           
           8"""

tree_1_windows = u"""          8^8
         8^^^8
        8^^^^^8
       8^^^^^^^8
      8^^^^^^^^^8
     8^^^^^^^^^^^8
    8^^^^^^^^^^^^^8
   8^^^^^^^^^^^^^^^8
  8^^^^^^^^^^^^^^^^^8
 8^^^^^^^^^^^^^^^^^^^8
8^^^^^^^^^^^^^^^^^^^^^8"""

tree_trunk_windows = u"""           88
           88"""

if sys.platform.startswith('win'):
  lable  = u"С Новым Годом!"
  star = star_windows
  tree_head = tree_head_windows
  tree_1 = tree_1_windows
  tree_trunk = tree_trunk_windows
  ball_symbol = "*"
  symbol_4_ball_set = "^"
  symbol_4_tree_trunk_change = "8"
else:
  lable = u"С Новым Годом!\n"#lable_linux
  star = star_linux
  tree_head = tree_head_linux
  tree_1 = tree_1_linux
  tree_trunk = tree_trunk_linux
  ball_symbol = u"✹"
  symbol_4_ball_set = u"▓"
  symbol_4_tree_trunk_change = u"█"



def set_color_balls_on_tree(tree="", symbol_4_ball_set="", ball_symbol = ""):
  from random import randint
  rows = tree.splitlines()
  max_count_4_replace = len(tree.split(symbol_4_ball_set))
  max_balls_count_on_tree = max_count_4_replace/3
  min_balls_count_on_tree = max_count_4_replace/5
  realy_balls_count_on_tree = randint(min_balls_count_on_tree, max_balls_count_on_tree)
  row_num = len(rows) - 1
  while row_num >= 0:
    l = len(rows[row_num].split(symbol_4_ball_set))-1
    if l:
      replace_count = randint(l/5, l/3)
      if (realy_balls_count_on_tree - replace_count) <=0 :
        replace_count = realy_balls_count_on_tree
      if replace_count:
        symbol_step_len = l/replace_count
        a = rows[row_num].index(symbol_4_ball_set)
        start_symbol_num = randint(a,a+1)
        l = list(rows[row_num])
        while start_symbol_num < len(l)-1:
          l[start_symbol_num] = ball_symbol
          start_symbol_num += symbol_step_len
        rows[row_num] = ""
        for i in l:
          rows[row_num] += unicode(i)
        max_count_4_replace = max_count_4_replace - replace_count
    row_num -= 1
  return rows

tree_body = [set_color_balls_on_tree(tree_1, symbol_4_ball_set, ball_symbol) for i in xrange(0,1,1)]

# for i in xrange(0,30,1):
#   print i
#   printout(unicode(" "), i)

# sys.stdout.write("\x1b[1;%dm" % (30 + 13) + u" " + "\x1b[0m")

def show_all(star="", tree_head="", tree_body="", lable="", text=""):
  i = 0
  star_color = [WHITE, YELLOW, RED]
  j = 0
  while True:
    printout(lable)
    printout(star, star_color[j])
    print tree_head
    for row in tree_body[i]:
      for s in row:
        if unicode(s) == ball_symbol:
          printout(unicode(s), random.randint(1, 7))
        else:
          printout(unicode(s), GREEN)
      print
    for s in tree_trunk:
      if s == symbol_4_tree_trunk_change:
        printout(u" ",13)
      else:
          printout(unicode(s), GREEN)
    print
    printout(text, WHITE)

    if j < len(star_color)-1:
      j += 1
    else:
      j = 0

    if i < len(tree_body)-1:
      i += 1
    else:
      i = 0
    time.sleep(1)

show_all(star, tree_head, tree_body, lable, text)
