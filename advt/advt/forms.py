# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:06:15 2022

@author: Vaibhav Tiwari
"""
from django import forms

class usersForm(forms.Form):
    n1=forms.CharField(label="Value 1")
    n2=forms.CharField(label="Value 2")
    
    
    
    
'''<form method="post">
  <div>
  <label for = "">Value 1</label>
  <input type="text" name="num1" value="{{n1}}" class = "form-control"/>
  </div>
  <div>
  <label for =""> Value 2 </label>
  <input type = "text" name="num2" value="{{n2}}" class="form-control"/>
  </div>
  <button type="submit">Save</button>
  output
  <input type"text" value="{{output}}"/>
</form>'''