#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
__author__ = 'nullexception'
import sys
import time
import sys
from power_console import *
import random

date = """
★░★░★░★░▀▀▀▀█░░█▀▀▀█░░▀█░░█░░░█░★░★░★░★ 
★░★░★░★░█▀▀▀▀░░█░░░█░░░█░░▀▀▀▀█░★░★░★░★ 
★░★░★░★░▀▀▀▀▀░░▀▀▀▀▀░░░▀░░░░░░▀░★░★░★░★"""

lable = """
✷░░░█▀▀░░█░█░█▀█░█▀█░░█░░░█░█▀▌░▐▀█░░░✷
❂░░░█░░░░█▀█░█░█░█▀▀█░█▀█░█░█░▀█▀░█░░░❂
✹░░░▀▀▀░░▀░▀░▀▀▀░▀▀▀▀░▀▀▀░▀░▀░░▀░░▀░░░✹
✶░░░░░░█▀▀░█▀█░░█▀█░░█▀█░█▀▌░▐▀█░░░░░░✶
✳░░░░░░█░░░█░█░░█░█░░█░█░█░▀█▀░█░░░░░░✳
✸░░░░░░▀░░░▀▀▀░▐▀▀▀▌░▀▀▀░▀░░▀░░▀░░░░░░✸
"""

text = """
Дорогие друзья! Поздравляю вас с Новым 2014 годом!
Желаю всем вам в наступающем году много новых и интересных задач!
Чтобы количество начатых проектов равнялось количеству успешных релизов!
Также желаю вам, чтобы вы реже встречались с синьором Dead_Line-ом!
Дорогие друзья, желаю, чаще покидать околокопьютерное-диванное пространство и 
проводить время вместе с друзьми, любимыми и близкими вам людьми 
(поверьте им вас не хватает).
"""

tree_0 = """  ★                                  
              8                                      
             G8I                                      
            OZ7$D                                  
           56+~I?8                                  
          ZZ$ZZZ$OZ                                  
         $?=?I=II+?8                                  
        8OZZZZZZZZZ8O                               
       9=ZI=??=?I+I$+D                               
      OZ$8O$ZZ$ZZZO8OZ8                               
     0Z?=ZI+I?+II?IZ?=;F                               
    ZOOZ$OZ$$Z$Z$ZZOZ7OOZO                            
   $I+$++Z?+II=???I$?=$?+DR                            
  DO7IZ77O$?7$I7$77O7IZ7I8TY                            
 II+Z?+Z?+ZI=?I=I?+IZ?=$+=$?I                         
D$$7Z7IZ77Z7I7$I777$Z7IZ7IZ7I7                         
            DI+?                                      
            D$77                                     
"""

star = """
           ★"""

tree_head = u"""           
           █"""

tree_1 = u"""          █▓█
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

tree_trunk = """           ██
           ██"""



def set_color_balls_on_tree(tree="", symbol_4_ball_set="", ball_symbol = ""):
  from random import randint
  # tree = tree.replace(" ", "")
  # print tree
  rows = tree.splitlines()
  # max_len = len(max(rows).split(symbol_4_ball))
  max_count_4_replace = len(tree.split(symbol_4_ball_set))
  max_balls_count_on_tree = max_count_4_replace/3
  min_balls_count_on_tree = max_count_4_replace/5
  realy_balls_count_on_tree = randint(min_balls_count_on_tree, max_balls_count_on_tree)
  # print "max_count_4_replace: ", max_count_4_replace
  # print "max_balls_count_on_tree: ", max_balls_count_on_tree
  # print "min_balls_count_on_tree: ", min_balls_count_on_tree
  # print "realy_balls_count_on_tree: ", realy_balls_count_on_tree
  row_num = len(rows) - 1
  while row_num >= 0:
    l = len(rows[row_num].split(symbol_4_ball_set))-1
    if l:
      replace_count = randint(l/5, l/3)
      if realy_balls_count_on_tree - replace_count and replace_count:
        symbol_step_len = l/replace_count
        a = rows[row_num].index(symbol_4_ball_set)
        start_symbol_num = randint(a,a+1)
        # print start_symbol_num
        l = list(rows[row_num])
        while start_symbol_num < len(l)-1:
          l[start_symbol_num] = ball_symbol
          start_symbol_num += symbol_step_len
        rows[row_num] = u""
        for i in l:
          rows[row_num] += unicode(i)
        # print rows[row_num]
        max_count_4_replace = max_count_4_replace - replace_count
    row_num -= 1
  # for i in rows:
    # print i
  return rows

ball_symbol = u"✹"
symbol_4_ball_set = u"▓"
tree_body = set_color_balls_on_tree(tree_1, symbol_4_ball_set, ball_symbol)
while True:
  printout(lable)
  printout(star, YELLOW)
  print tree_head
  for row in tree_body:
    for s in row:
      if unicode(s) == ball_symbol:
        printout(unicode(s), random.randint(1, 7))
      else:
        printout(unicode(s), GREEN)
    print 
  printout(tree_trunk,GREEN)
  print
  printout(text, RED)
  # printout(date)
  time.sleep(1)

