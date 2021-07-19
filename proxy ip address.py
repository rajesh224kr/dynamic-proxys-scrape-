from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def Porxy_IP():
	
    try:
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(1366, 786))
        display.start()
    except Exception:
        pass
    chrome_options = Options()
    driver = webdriver.Chrome(chrome_options=chrome_options)
    url ='https://www.sslproxies.org/'
    driver.get(url)
    time.sleep(5)
    # Pass the name of the country whose IP address is required
    country_name = 'India'
    try:
        driver.find_element_by_css_selector('div.dataTables_filter label:nth-child(1) > input.form-control.input-sm').send_keys(country_name)
        time.sleep(5)
    except:
        pass
    time.sleep(5)
    # proxy_tables = driver.find_elements_by_css_selector('#proxylisttable tbody tr')
    proxy_tables = driver.find_elements_by_css_selector('#proxylisttable tbody tr1')
    proxy_table_len = len(proxy_tables)
    print(proxy_table_len)
    if(proxy_table_len>1):
        print('Proxy address Found: url >> 1')
        final_ip_port = []
        for p_table in proxy_tables:
            country = p_table.find_element_by_css_selector('td:nth-of-type(3)').text
            print('Country :' , country)
            ip_address = p_table.find_element_by_css_selector('td:nth-of-type(1)').text
            port = p_table.find_element_by_css_selector('td:nth-of-type(2)').text
            print(ip_address+':'+port)
            ip_port = ip_address+':'+port
            final_ip_port.append(ip_port)
        
        try:
            display.stop()
            
        except:
            pass
        driver.quit()
        return final_ip_port

    # if in case ip address is less then one 
    elif(proxy_table_len<1):
        
        url ='https://free-proxy-list.net/anonymous-proxy.html'
        driver.get(url)
        time.sleep(5)

        print('-----------------------------------------')
        print('URL 2 : ' , url)
        print('------------------------------------------')
        # Pass the name of the country whose IP address is required
        country_name = 'India'
        try:
            driver.find_element_by_css_selector('div.dataTables_filter label:nth-child(1) > input.form-control.input-sm').send_keys(country_name)
            time.sleep(5)
        except:
            pass
        time.sleep(5)
        # proxy_tables = driver.find_elements_by_css_selector('#proxylisttable tbody tr')
        proxy_tables = driver.find_elements_by_css_selector('#proxylisttable tbody tr1')
        
        proxy_table_len = len(proxy_tables)
        print(proxy_table_len)
        if(proxy_table_len<1):
            driver.quit()
        print('Proxy address Found: url >>2')
        final_ip_port = []
        for p_table in proxy_tables:
            country = p_table.find_element_by_css_selector('td:nth-of-type(3)').text
            print('Country :' , country)
            ip_address = p_table.find_element_by_css_selector('td:nth-of-type(1)').text
            port = p_table.find_element_by_css_selector('td:nth-of-type(2)').text
            print(ip_address+':'+port)
            ip_port = ip_address+':'+port
            
            final_ip_port.append(ip_port)

        try:
            display.stop()
        except:
            pass
        driver.quit()
        return final_ip_port
    else:
        print('None >> proxy ')
        return None
a = Porxy_IP()
print(a)
# get list of ip address >> leasted ip address 
print('-------------------------------------')
print('----------end ip address ------------')
print('-------------------------------------')