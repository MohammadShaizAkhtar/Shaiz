# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:11:52 2020

@author: SHAIZ
"""

class node:
    def __init__(self):
        self.m_children_nodes={}
        self.m_total_word_so_far=''
        self.m_current_letter=''
        self.m_word=''
        self.m_curr_index=0
    def add_word(self,word,word_so_far='',curr_index=-1):
        self.m_word=word
        self.m_curr_index=curr_index
        if self.m_curr_index>=0:
            self.m_current_letter=self.m_word[self.m_curr_index]
            self.m_total_word_so_far=word_so_far + self.m_word[self.m_curr_index]
        if self.m_curr_index+1<len(self.m_word):
            if self.m_word[self.m_curr_index+1] not in self.m_children_nodes:
                self.m_children_nodes[self.m_word[self.m_curr_index+1]]=node()
                self.m_children_nodes[self.m_word[self.m_curr_index+1]].add_word(\
                                     self.m_word, self.m_total_word_so_far,self.m_curr_index+1)
            else:
                  self.m_children_nodes[self.m_word[self.m_curr_index+1]].add_word(\
                                      self.m_word, self.m_total_word_so_far,self.m_curr_index+1)
                 
                
       
    def auto_complete_word(self,str):
        if len(str)>0 and str[0] in self.m_children_nodes:
            self.m_children_nodes[str[0]].auto_complete_word(str[1:])
        if len(str)==0:
           # print("auto complete :")
            self.print_tree()
    def print_tree(self):
        if self:
            if len(self.m_children_nodes)==0:
                print('word : ',self.m_total_word_so_far)
            else:
                for i in self.m_children_nodes:
                    self.m_children_nodes[i].print_tree()



#client code
words=['a','ability','able','about','above','accept','according','account','across','act','action','and','baby','back','bad','bag','ball','bank','be','beautiful','because','bed','before','call','camera','campaign','can','cancer','candidate','dark','data','daughter','day','dead','deal','die','do','during','each','early','education','else','employee','end','dear','for','goat']
root=node()
for word in words:
    root.add_word(word)
#eroot.print_tree()
#root.auto_complete_word('ab')
for i in range(1):
    
    mystr=input('enter letter to autocomplete: ')
    root.auto_complete_word(mystr)
   