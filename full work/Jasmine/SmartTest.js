describe('SmartBear', () =>
{
        it('Should navigate to SmartBear Login Page', () => 
        {
            browser.get('http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx');
            browser.getCurrentUrl().then((url) => {
            expect(url).toBe('http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx');
        });
    
   
        it('Should accept the user login credentials and login', () => 
        {
            element (by.id ('ctl00_MainContent_username')).sendkeys ('Tester');
            element (by.id ('ctl00_MainContent_password')).sendkeys ('test345');
            element (by.id ('ctl00_MainContent_login_button')).click();
            expect(url).toBe('http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/default.aspx');
        });
    

        it('Should go to View all orders page', () => 
        {
            element (by.xpath ('/html/body/form/table/tbody/tr/td[1]/ul/li[1]/a')).click();
            expect(title).toBe('List of All Orders');
        }); 
    
        it('Should go to View all Product page ', () => {
            element (by.xpath ('/html/body/form/table/tbody/tr/td[1]/ul/li[2]/a')).click();
            expect(title).toBe('List of Products');
        }); 
    
        it('Should go to orders page and check title', () => {
            element (by.xpath ('/html/body/form/table/tbody/tr/td[1]/ul/li[3]/a')).click();
            expect(title).toBe('Order');
        });
    });
 }); 