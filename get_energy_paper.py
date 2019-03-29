# -*- coding: utf-8 -*-

from selenium import webdriver
import pickle

years = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

driver = webdriver.Chrome()

for year in years:
    
    page_url = "http://www.enecho.meti.go.jp/about/whitepaper/" + str(year) + "html/"
    
    driver.get(page_url)
    
    links = []
    
    for a_element in driver.find_elements_by_tag_name('a'):
        if a_element.get_attribute('href').find(page_url) != -1 and a_element.get_attribute('href').find(page_url + '#') == -1:
            links.append(a_element.get_attribute('href'))
    
    texts = []
    
    for link in links:
        driver.get(link)
        text = []
        for p_element in driver.find_elements_by_tag_name('p'):
            if p_element.get_attribute('class') == "" and len(p_element.text) > 50 and p_element.text.find('Adobe Acrobat Reader') == -1 and p_element.text.find('Copyright') == -1 and p_element.text.find('ppt/pptx形式') == -1:
                text.append(p_element.text)
        texts.append(text)
    
    fname = "energy_paper_" + str(year) + ".pickle"
    pickle.dump(texts, open(fname, 'wb'))