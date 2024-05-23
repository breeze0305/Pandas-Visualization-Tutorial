import pandas as pd
import gradio as gr
import random
class FunctionsClass():
    def __init__(self):
        self.hide = gr.Number(visible=False)
        self.text = gr.Markdown(visible=True)
        self.correct = gr.Image(value='correct.png',height=300,width=300,visible=True,interactive=False,show_download_button=False,show_label=False,show_share_button=False)
        self.wrong = gr.Image(value='wrong.png',height=300,width=300,visible=True,interactive=False,show_download_button=False,show_label=False,show_share_button=False)
        self.choices_q1 = {
                    "pandas.read_csv('data.csv')":0,
                    "pandas.read_csv('df.csv')":1,
                    "pandas.read_csv('data.xlsx')":2,
                    "read_csv('data.csv')":3,
                        }
        self.choices_q2 = {
                    "df.head()":0,
                    "df.tail()":1,
                        }
        self.choices_q3 = {
                    'D 博士':0,
                    'M 碩士':1,
                    'B 學士':2,
                    'X 4+X':3,
                    'C 二技':4,
                    'B 四技':5,
                    '5 五專':6,
                    '5 七年':7,
                    '2 二專':8,
                    'C 二年制':9
                        }
        self.choices_q6 = {
                    "df = df.drop_duplicates(subset=['學校名稱'])":0,
                    "df = df.sort_values(by='學校名稱')":1,
                        }
        self.mapping_q7 = {'臺北市':'北部','新北市':'北部','基隆市':'北部','新竹市':'北部','桃園市':'北部','新竹縣':'北部',
                    '宜蘭縣':'北部','臺中市':'中部','苗栗縣':'中部','彰化縣':'中部','南投縣':'中部','雲林縣':'中部','高雄市':'南部',
                    '臺南市':'南部','嘉義市':'南部','嘉義縣':'南部','屏東縣':'南部','澎湖縣':'南部','花蓮縣':'東部','臺東縣':'東部',
                    '金門縣':'福建省'}
        self.choices_q7_2 = {"data.to_csv('new_data.csv',encoding='utf-8-sig')":0,
                        "pandas.to_csv('new_data.csv',encoding='utf-8-sig')":1,
                        "pandas.csv('new_data.csv',encoding='utf-8-sig')":2,
                        "data.csv('new_data.csv',encoding='utf-8-sig')":3,
                        }  
        
    def q1_checkbox_fn(self,check_str,df_file): #data.csv
        check_idx = self.choices_q1.get(check_str,-1)
        if check_idx == 0:
            return gr.Dataframe(value=df_file,visible=True),self.hide #答對
        elif check_idx == 1:
            error = """
            Traceback (most recent call last):
                df = pandas.read_csv('df.csv')
                FileNotFoundError: [Errno 2] No such file or directory: 'df.csv'
            """
            return self.hide,gr.Textbox(value=error,visible=True)
        elif check_idx == 2:
            error = """
            Traceback (most recent call last):
                df = pandas.read_csv('data.xlsx')
                FileNotFoundError: [Errno 2] No such file or directory: 'data.xlsx'
            """
            return self.hide,gr.Textbox(value=error,visible=True)
        elif check_idx == 3:
            error = """
            Traceback (most recent call last):
                df = read_csv('data.csv')
                NameError: name 'read_csv' is not defined
            """
            return self.hide,gr.Textbox(value=error,visible=True)

    def q1_btm_fn(self,check_str):
        check_idx = self.choices_q1.get(check_str,-1)
        correct_text = """
                        恭喜答對！  
                        在讀取dataframe的時候，我們要使用pandas.read_csv()，並且在括號裡面填入要讀取的檔案名稱(包含附檔名)。  
                        如果'檔案'是以其他編碼寫的，那我們就要在括號裡面加上encoding='編碼'。  
                        例如:  
                        ```  
                        df = pandas.read_csv('data.csv',encoding='utf-8')  
                        ```  
                        請繼續第二題！  
                        """
        wrong_text = """
                    答錯囉！  
                    請仔細查看按下對應按鈕後，結果的變化。  
                    並仔細檢查每個選項之間的不同！  
                    按下F5刷新網頁重新答題！  
                    """
        if check_idx == 0:
            return self.correct,gr.Markdown(value=correct_text,visible=True),self.hide,self.hide,self.hide,self.hide
        else:
            return self.wrong,gr.Markdown(value=wrong_text,visible=True),self.hide,self.hide,self.hide,self.hide
        
    def q2_checkbox_fn(self,check_str,dataframe):
        check_idx = self.choices_q2.get(check_str,-1)
        if check_idx == 0:
            return gr.Dataframe(value=dataframe.head(),height=200,visible=True,interactive=False),gr.Number(label='輸入head()裡面的數字',visible=True,interactive=True)
        elif check_idx == 1:
            return gr.Dataframe(value=dataframe.tail(),height=200,visible=True,interactive=False),gr.Number(label='輸入tail()裡面的數字',visible=True,interactive=True)
    
    def q2_number_fn(self,number,check_str,dataframe):
        check_idx = self.choices_q2.get(check_str,-1)
        if check_idx == 0:
            temp = dataframe.head(number)
        elif check_idx == 1:
            temp = dataframe.tail(number)
        
        print(temp)
        return gr.Dataframe(value=temp,height=400,visible=True)
    def q2_btm_fn(self,check_str,number):
        check_idx = self.choices_q2.get(check_str,-1)
        correct_text = """
                        恭喜答對！  
                        使用```.head()```可以從dataframe中讀取前幾筆資料。
                        使用```.tail()```可以從dataframe中讀取後幾筆資料。
                        括號裡面則可以填入要讀取的筆數。  
                        請繼續第三題！  
                        """
        wrong_text = """
                    答錯囉！  
                    請仔細查看按下對應按鈕後，結果的變化。  
                    並仔細檢查每個選項之間的不同！  
                    按下F5刷新網頁重新答題！  
                    """
        if check_idx == 0 and number == 5:
            return self.correct,gr.Markdown(value=correct_text,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide
        else:
            return self.wrong,gr.Markdown(value=wrong_text,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide
        
    def q3_read_level(self):
        df = pd.read_csv('data.csv') 
        unique_values = df["等級別"].unique()
        return list(unique_values)
    
    def q3_checkbox_fn(self,check_str,dataframe):
        return gr.Dataframe(value=dataframe[dataframe['等級別'] == check_str],visible=True),gr.Radio(visible=True),gr.Radio(visible=True),gr.Markdown(visible=True)
    
    def q3_read_column(self):
        df = pd.read_csv('data.csv') 
        return list(df.columns)
    
    def q3_checkbox2_fn(self,check_str,check_ascending,dataframe):
        if check_ascending == 'True':
            check_ascending = True
        else:
            check_ascending = False
        if not check_str:
            return self.hide
        df = dataframe.sort_values(by=str(check_str), ascending=check_ascending)
        return gr.Dataframe(value=df,visible=True)
    
    def q3_btm_fn(self,check_str1,check_str2,check_str3):
        #check_box1_q3,check_box2_q3,ascending_check_box3_q3
        correct_text = """
                        恭喜答對！  
                        透顧``` df['等級別'] == 'D 博士'```可以將'等級別'中有'D 博士'的欄位保留
                        再透過sort_values來對'總計'進行排序，便可以找出博士最多的學校。
                        當ascending是True時，sort排序為由小到大。
                        所以如果我們要透過df.head(1)來印出最多博士的學校時，就要將ascending設為False。
                        ```  
                        df = df.sort_values(by='總計', ascending=False)
                        ```  
                        請繼續第四題！  
                        """
        wrong_text = """
                    答錯囉！  
                    請仔細查看按下對應按鈕後，程式碼的變化。  
                    並仔細檢查每個選項之間的不同！  
                    按下F5刷新網頁重新答題！  
                    """
        check_idx1 = self.choices_q3.get(check_str1,-1) # 0 correct
        choices2_q3 = {'總計':0}
        check_idx2 = choices2_q3.get(check_str2,-1) # 0 correct
        choices3_q3 = {'False':0}
        check_idx3 = choices3_q3.get(check_str3,-1) # 0 correct
        if check_idx1 == 0 and check_idx2 == 0 and check_idx3 == 0:
            return self.correct,gr.Markdown(value=correct_text,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide
        else:
            return self.wrong,gr.Markdown(value=wrong_text,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide
    
    def q4_read_column(self):
        df = pd.read_csv('data.csv') 
        return list(df.columns)
    
    def q4_checkbox1_fn(self,check_str):
        if check_str is None:
            return self.hide,self.hide,self.hide
        elif check_str == '總計':
            return self.hide,self.hide,self.hide

        df = pd.read_csv('data.csv')
        df1 = df.groupby(str(check_str))['總計'].sum()
        df2 = df1.reset_index()
        return gr.Dataframe(value=df2,height=400,visible=True),gr.Markdown(visible=True),gr.Radio(visible=True)
    
    def q4_checkbox2_fn(self,check_str1, check_str2):
        df = pd.read_csv('data.csv')
        df1 = df.groupby(str(check_str2))['總計'].sum()
        df2 = df1.reset_index()
        df3 = df2.sort_values(by=str(check_str1), ascending=False)
        return gr.Dataframe(value=df3,height=400,visible=True)
    
    def q4_btm_fn(self, check_str1, check_str2):
        correct_text = """
                    恭喜答對！  
                    我們可以利用程式對某個Column做分組，再逐一判斷dataframe裡面有相關的關鍵字的data，這樣的方法可以讓我們在處理大量資料時，可以直接做簡單的計算。  
                    再透過sort_values來對'總計'進行排序，便可以找出總人數最多的學校。
                    當ascending是True時，sort排序為由小到大。  
                    """
        wrong_text = """
                    答錯囉！  
                    請仔細查看按下對應按鈕後，程式碼的變化。  
                    並仔細檢查每個選項之間的不同！  
                    按下F5刷新網頁重新答題！  
                    """
        if check_str1 == '學校名稱' and check_str2 == '總計':
            return self.correct,gr.Markdown(value=correct_text,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide
        else:
            return self.wrong,gr.Markdown(value=wrong_text,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide

    def q5_checkbox_fn(self,check_str,dataframe):
        df = pd.DataFrame(dataframe[check_str])
        return gr.Dataframe(value=df,height=400,visible=True),gr.Radio(visible=True),gr.Markdown(visible=True)
    
    def q5_textbox_fn(self,str_in,df,column):
        if ' ' in str_in:
            m , n = str_in.split(' ',1)
        else:
            return self.hide,self.hide
        n = n if n != '' else 'dmnkdnfsm,nfmd'
        m_count = df[column].str.contains(m).sum()
        n_count = df[column].str.contains(n).sum()
        pub_num = int(m_count+n_count)
        total = int(df.shape[0]) # total row
        
        return gr.Number(value=pub_num,visible=True),gr.Number(value=total-pub_num,visible=True)
        
    def q5_btm_fn(self,check_str1,check_str2):
        correct_text = """
                        恭喜答對！  
                        我們可以利用程式先提取出某個Column，再逐一判斷dataframe裡面有相關的關鍵字的data，這樣的方法可以讓我們在處理大量資料時，可以直接做簡單的計算。  
                        但要注意某些類別資料的關鍵字不只一種,需要全部考慮進來喔~
                        例如:  
                        '國立'與'市立'都算是國立的大學  
                        """
        wrong_text = """
                    答錯囉！  
                    請仔細查看按下對應按鈕後，程式碼的變化。  
                    並仔細檢查每個選項之間的不同！  
                    按下F5刷新網頁重新答題！  
                    """
        if check_str1 == '學校名稱' and check_str2 == "國立 市立":
            return self.correct,gr.Markdown(value=correct_text,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide
        else:
            return self.wrong,gr.Markdown(value=wrong_text,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide
    
    def q6_checkbox_fn(self,check_str,dataframe):
        check_idx = self.choices_q6.get(check_str,-1)
        if check_idx == 0:
            df = dataframe.drop_duplicates(subset=['學校名稱'])
            return gr.Dataframe(value=df,height=300,visible=True),gr.Number(value=47,visible=True),gr.Number(value=98,visible=True)
        else:
            df = dataframe.sort_values(by='學校名稱')
            return gr.Dataframe(value=df,height=300,visible=True),gr.Number(value=239,visible=True),gr.Number(value=525,visible=True)

    def q6_btm_fn(self,check_str):
    #check_box1_q3,check_box2_q3,ascending_check_box3_q3
        correct_text = """
                        恭喜答對！
                        我們可以利用程式，提取出dataframe裡面有相關的關鍵字的data，  
                        這樣的方法可以讓我們在處理大量資料時，可以直接做簡單的計算。但同時在做資料計算時，我們要非常小心，需要觀察資料類型，  
                        不可以將重複的資料當成新資料去計算，這樣會導致結果與我們想要的不符。   
                        """
        wrong_text = """
                    答錯囉！  
                    請仔細查看按下對應按鈕後，程式碼的變化。  
                    並仔細檢查每個選項之間的不同！  
                    按下F5刷新網頁重新答題！  
                    """
        correct_code = """
                    ```python
                    df = df.drop_duplicates(subset=['學校名稱'])
                    """
        wrong_code = """
                    ```python
                    df = df.sort_values(by='學校名稱')
                    """
        check_idx = self.choices_q6.get(check_str,-1)
        if check_idx == 0:
            return self.correct,gr.Markdown(value=correct_text,visible=True),gr.Markdown(value=correct_code,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide,self.hide
        else:
            return self.wrong,gr.Markdown(value=wrong_text,visible=True),gr.Markdown(value=wrong_code,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide,self.hide
        
    def q7_checkbox_fn(self,check_str): 
        data = self.q7_data1_fn()
        data['地區'] = data[check_str].map(self.mapping_q7)
        return gr.Dataframe(value=data,visible=True),gr.Radio(visible=True)

    def q7_checkbox2_fn(self,check_str): #data.csv
        check_idx = self.choices_q7_2.get(check_str,-1)
        if check_idx == 0:
            data = self.q7_data1_fn()
            data['地區'] = data['縣市名稱'].map(self.mapping_q7)
            data.to_csv('new_data.csv',encoding='utf-8-sig')
            return self.hide,gr.File(value='new_data.csv',visible=True) #答對
        elif check_idx == 1:
            error = """
            Traceback (most recent call last):
                pandas.to_csv('new_data.csv',encoding='utf-8-sig')
            AttributeError: module 'pandas' has no attribute 'to_csv'
            """
            return gr.Textbox(value=error,visible=True),self.hide
        elif check_idx == 2:
            error = """
            Traceback (most recent call last):
                pandas.csv('new_data.csv',encoding='utf-8-sig')
            AttributeError: module 'pandas' has no attribute 'csv'
            """
            return gr.Textbox(value=error,visible=True),self.hide
        elif check_idx == 3:
            error = """
            Traceback (most recent call last):
            AttributeError: 'DataFrame' object has no attribute 'csv'. Did you mean: 'cov'?  
            """
            return gr.Textbox(value=error,visible=True),self.hide
            
    def q7_btm_fn(self,check_str,check_str2):
        check_idx_2 = self.choices_q7_2.get(check_str2,-1)
        correct_text = """
                        恭喜答對！  
                        在新增欄時如果要依據字典表映射填入，應使用.map()，並在括號裡面填入要映射字典的名稱。    
                        例如:  
                        ```  
                        data['地區'] = data['縣市名稱'].map(region_mapping) 
                        ``` 
                        而在轉換dataframe到csv的時候，我們要使用.to_csv()，並在括號裡面填入要存取的檔案名稱(包含附檔名)。  
                        括號裡面可以加上encoding='編碼'，以防止亂碼。  
                        例如:  
                        ```  
                        data.to_csv('new_data.csv',encoding='utf-8-sig')  
                        ```  
                        """
        wrong_text = """
                    答錯囉！  
                    請仔細查看按下對應按鈕後，結果的變化。  
                    並仔細檢查每個選項之間的不同！  
                    按下F5刷新網頁重新答題！  
                    """
        if check_str=='縣市名稱' and check_idx_2 == 0:
            return self.correct,gr.Markdown(value=correct_text,visible=True),gr.DownloadButton(value='new_data.csv',visible=True),self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide
        else:
            return self.wrong,gr.Markdown(value=wrong_text,visible=True),self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide,self.hide
    def q7_data1_fn(self):
        data = pd.read_csv('data.csv')
        def remove_numbers(city_name):
            return ''.join([char for char in city_name if not char.isdigit()]).strip()
        data['縣市名稱'] = data['縣市名稱'].apply(remove_numbers)
        return data
    
    def q7_data2_fn(self):
        data_items = self.mapping_q7.items()
        data_list = list(data_items)
        df = pd.DataFrame(data_list, columns=['縣市', '區域'])
        return df
    
    def q7_read_column(self):
        df = pd.read_csv('data.csv') 
        x = list(df.columns)
        random.shuffle(x)
        return x