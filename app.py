import gradio as gr
import pandas as pd
import random
import time
from fn import FunctionsClass

def correct(user,password):
    return user == 'aaa' and password == '1234'
    
def main():
    fn = FunctionsClass()
    # Displaying the styled dataframe in Gradio
    
    with gr.Blocks() as demo:
        with gr.Tab(label='問題一'):
            gr.Markdown("""
                        ### 問題一  
                        我想讀取這個指定的csv  
                        ```python
                        import pandas  
                        ...  
                        ```
                        """)
            file_q1 = gr.File(value='data.csv',visible=True)
            choices_q1 = ["pandas.read_csv('data.csv')",
                        "pandas.read_csv('df.csv')",
                        "pandas.read_csv('data.xlsx')",
                        "read_csv('data.csv')",
                        ]
            random.shuffle(choices_q1)
            check_box_q1 = gr.Radio(choices=choices_q1,label='choose the correct function',value=False)
            show_df_q1 = gr.Dataframe(visible=False)
            error_text_q1 = gr.Textbox(visible=False)
            submit_btm_q1 = gr.Button(value='Submit',variant='primary',visible=True)
            with gr.Row():
                with gr.Column(scale=1):
                    ans_pic_q1 = gr.Image(visible=False)
                with gr.Column(scale=2):
                    ans_word_q1 = gr.Markdown(value='test',visible=False)
        check_box_q1.select(fn.q1_checkbox_fn,inputs=[check_box_q1,file_q1],outputs=[show_df_q1,error_text_q1])
        submit_btm_q1.click(fn.q1_btm_fn,inputs=[check_box_q1],outputs=[ans_pic_q1,ans_word_q1,show_df_q1,check_box_q1,error_text_q1,submit_btm_q1])
        with gr.Tab(label='問題二'):
            gr.Markdown("""
                        ### 問題二  
                        我已經讀取dataframe了,接下來我想印出指定csv的前5個row  
                        ```python
                        import pandas  
                        df = pandas.read_csv('data.csv') 
                        ```
                        """)
            choices_q2 = [
                        "df.head()",
                        "df.tail()",
                        ]
            random.shuffle(choices_q2)
            show_df_q2 = gr.Dataframe(value='data.csv',visible=True,label='原始數據',height=200,interactive=False)
            check_box_q2 = gr.Radio(choices=choices_q2,label='choose the correct function',value=False)
            show_df_q2_after = gr.Dataframe(visible=False)
            enter_number_q2 = gr.Number(visible=False)
            show_df_q2_after_after = gr.Dataframe(visible=False)
            submit_btm_q2 = gr.Button(value='Submit',variant='primary',visible=True)
            with gr.Row():
                with gr.Column(scale=1):
                    ans_pic_q2 = gr.Image(visible=False)
                with gr.Column(scale=2):
                    ans_word_q2 = gr.Markdown(value='test',visible=False)
                # ans_word_q2 = gr.Markdown(visible=False)
        check_box_q2.select(fn.q2_checkbox_fn,
                            inputs=[check_box_q2,show_df_q2],
                            outputs=[show_df_q2_after,enter_number_q2])
        enter_number_q2.change(fn.q2_number_fn,
                                inputs=[enter_number_q2,check_box_q2,show_df_q2],
                                outputs=[show_df_q2_after_after])
        submit_btm_q2.click(fn.q2_btm_fn,
                            inputs=[check_box_q2,enter_number_q2],
                            outputs=[ans_pic_q2,ans_word_q2,submit_btm_q2,check_box_q2,show_df_q2,enter_number_q2,show_df_q2_after_after])
        with gr.Tab(label='問題三'):
            gr.Markdown("""
                        ### 問題三  
                        我已經讀取dataframe了,印出有招生"D 博士"的學校數量並且排序列印出來(由大到小),  
                        然後再印出最多博士的學校。  
                        ```python
                        import pandas  
                        df = pandas.read_csv('data.csv')  
                        df = df[df['等級別'] == ' X ']  
                        ```
                        """)
            choices1_q3 = fn.q3_read_level()
            show_df_q3 = gr.Dataframe(value='data.csv',visible=True,label='原始數據',height=200,interactive=False)
            random.shuffle(choices1_q3)
            check_box1_q3 = gr.Radio(choices=choices1_q3,label="choose the value of 'X'",value=False)
            show_df_q3_after = gr.Dataframe(visible=False,interactive=False)
            markdown_q3 = gr.Markdown("``` df = df.sort_values(by='X', ascending=...)```",visible=False)
            choices2_q3 = fn.q3_read_column()
            # random.shuffle(choices2_q3)
            check_box2_q3 = gr.Radio(choices=choices2_q3,label='sort by column name(X)',value=False,visible=False,interactive=True)
            choices3_q3 = ['True','False']
            ascending_check_box3_q3 = gr.Radio(choices=choices3_q3,label='ascending(bool)',value=False,visible=False,interactive=True)
            show_df_q3_after_after = gr.Dataframe(visible=False,interactive=False)
            submit_btm_q3 = gr.Button(value='Submit',variant='primary',visible=True)
            with gr.Row():
                with gr.Column(scale=1):
                    ans_pic_q3 = gr.Image(visible=False)
                with gr.Column(scale=2):
                    ans_word_q3 = gr.Markdown(value='test',visible=False)
        check_box1_q3.select(fn.q3_checkbox_fn,
                            inputs=[check_box1_q3,show_df_q3],
                            outputs=[show_df_q3_after,check_box2_q3,ascending_check_box3_q3,markdown_q3])
        check_box2_q3.select(fn.q3_checkbox2_fn,
                            inputs=[check_box2_q3,ascending_check_box3_q3,show_df_q3_after],
                            outputs=[show_df_q3_after_after])
        ascending_check_box3_q3.select(fn.q3_checkbox2_fn,
                            inputs=[check_box2_q3,ascending_check_box3_q3,show_df_q3_after],
                            outputs=[show_df_q3_after_after])
        submit_btm_q3.click(fn.q3_btm_fn,
                            inputs=[check_box1_q3,check_box2_q3,ascending_check_box3_q3],
                            outputs=[ans_pic_q3,ans_word_q3,submit_btm_q3,show_df_q3_after_after,ascending_check_box3_q3,check_box2_q3,markdown_q3,show_df_q3_after,check_box1_q3])
        
        with gr.Tab(label='問題四'):
            gr.Markdown("""
                        ### 問題四  
                        我已經讀取dataframe了,接下來我想印出每間學校的總人數,再按照總人數由大到小排列。  
                        ```python
                        import pandas

                        df = pandas.read_csv("data.csv")
                        data = df.groupby('X')['總計'].sum()
                        ```
                        """)
            show_df_q4 = gr.Dataframe(value = 'data.csv', visible=True, label='原始數據', height=200, interactive=False)
            choices1_q4 = fn.q4_read_column()
            check_box_1_q4 = gr.Radio(choices=choices1_q4, label='choose the value of X',visible=True,interactive=True)
            show_df_q4_after = gr.Dataframe(visible=False, height=200, interactive=False)
            markdown_1_q4 = gr.Markdown("""```python
                                        data = data.reset_index()  
                                        data = data.sort_values(by='Y', ascending=False)
                                        ```""",visible=False)
            choices2_q4 = fn.q4_read_column()
            check_box_2_q4 = gr.Radio(choices=choices2_q4,label="choose the value of 'Y'",visible=False,value=False)
            
            show_df_q4_after2 =  gr.Dataframe(visible=False, height=200, interactive=False)   
            submit_btm_q4 = gr.Button(value='Submit',variant='primary',visible=True)
            with gr.Row():
                with gr.Column(scale=1):
                    ans_pic_q4 = gr.Image(visible=False)
                with gr.Column(scale=2):
                    ans_word_q4 = gr.Markdown(value='test',visible=False)
        check_box_1_q4.select(fn.q4_checkbox1_fn,
                            inputs=[check_box_1_q4],
                            outputs=[show_df_q4_after, markdown_1_q4, check_box_2_q4])
        check_box_2_q4.select(fn.q4_checkbox2_fn,
                            inputs=[check_box_2_q4, check_box_1_q4],
                            outputs=[show_df_q4_after2])
        submit_btm_q4.click(fn.q4_btm_fn,
                            inputs=[check_box_1_q4, check_box_2_q4],
                            outputs=[ans_pic_q4, ans_word_q4, submit_btm_q4, show_df_q4_after2, check_box_2_q4, show_df_q4_after, markdown_1_q4, check_box_1_q4, show_df_q4])

            
        with gr.Tab(label='問題五'):
            gr.Markdown("""
                        ### 問題五  
                        我已經讀取dataframe了,我現在想要提取出所有公私立學校的dataframe,這段程式碼首先初始化兩個計數器,  
                        一個用來計數公立學校,另一個用來計數私立學校.然後,它會遍歷 Dataframe 中的每一行,  
                        計算dataframe裡面國立學校和私立學校出現的頻率. (包含重複出現的)  
                        請依序回答「X」、「M」、「N」  
                        ```python
                        import pandas  
                        df =pandas.read_csv('data.csv')  
                        public_count_all = 0
                        private_count_all = 0

                        for i in df['X']:
                            if 'M' in name or 'N' in name:
                                public_count_all += 1
                            else:
                                private_count_all += 1
                        ```
                        """)
            choices1_q5 = fn.q3_read_column()
            show_df_q5 = gr.Dataframe(value='data.csv',visible=True,label='原始數據',height=200,interactive=False)
            check_box1_q5 = gr.Radio(choices=choices1_q5,label="choose the value of 'X'",value=False)
            show_df_q5_after = gr.Dataframe(visible=False,interactive=False)
            markdown_q5 = gr.Markdown("```if 'M' in name or 'N' in name: ```",visible=False)
            choices2_q5 = gr.Textbox(label='請輸入「M」和「N」，並用空白隔開(請觀察上面的dataframe中的規律) 例如：私立 私立',visible=False,interactive=True)
            with gr.Row():
                public_num = gr.Number(label='公立學校出現的頻率(public_count_all)',visible=False,interactive=False)
                private_num = gr.Number(label='私立學校出現的頻率(private_count_all)',visible=False,interactive=False)
                
            submit_btm_q5 = gr.Button(value='Submit',variant='primary',visible=True)
            with gr.Row():
                with gr.Column(scale=1):
                    ans_pic_q5 = gr.Image(visible=False)
                with gr.Column(scale=2):
                    ans_word_q5 = gr.Markdown(value='test',visible=False)
        check_box1_q5.select(fn.q5_checkbox_fn,
                            inputs=[check_box1_q5,show_df_q5],
                            outputs=[show_df_q5_after,choices2_q5,markdown_q5])
        choices2_q5.change(fn.q5_textbox_fn,inputs=[choices2_q5,show_df_q5_after,check_box1_q5],outputs=[public_num,private_num] )
        submit_btm_q5.click(fn.q5_btm_fn,
                            inputs=[check_box1_q5,choices2_q5],
                            outputs=[ans_pic_q5,ans_word_q5,submit_btm_q5,markdown_q5,show_df_q5_after,check_box1_q5,show_df_q5,choices2_q5,public_num,private_num])
        
        with gr.Tab(label='問題六'):
            gr.Markdown("""
                        ### 問題六
                        在上一題中，我從資料中提取出了"學校名稱"的表格，但有很多資料是重複的，現在我需要計算有多少間學校(不重複)。  
                        接續上一題，我需要在計算學校前，先把重複的名稱刪除，這樣計算出來的數量才會是正確的。   
                        ```python 
                        import pandas  
                        df =pandas.read_csv('data.csv')  
                        public_count_all = 0
                        private_count_all = 0
                        ...
                        ```
                        """)
            show_df_q6 = gr.Dataframe(value='data.csv',label='原始數據',height=300,visible=True,interactive=False)
            choices_q6 = ["df = df.drop_duplicates(subset=['學校名稱'])","df = df.sort_values(by='學校名稱')"]
            random.shuffle(choices_q6)
            check_box_q6 = gr.Radio(choices=choices_q6,label="choose choose'",value=False)
            show_df_q6_after = gr.Dataframe(visible=False,interactive=False)
            correct_md = gr.Markdown()
            gr.Markdown("""
                        ```python
                        for name in df['學校名稱']:
                            if '國立' in name or '市立' in name:
                                public_count_all += 1
                            else:
                                private_count_all += 1
                        ```
                        """)
            with gr.Row():
                public_num = gr.Number(value=239,label='公立學校數量(不重複)public_count_all',visible=True,interactive=False)
                private_num = gr.Number(value=525,label='私立學校數量(不重複)private_count_all',visible=True,interactive=False)
            submit_btm_q6 = gr.Button(value='Submit',variant='primary',visible=True)
            with gr.Row():
                with gr.Column(scale=1):
                    ans_pic_q6 = gr.Image(visible=False)
                with gr.Column(scale=2):
                    ans_word_q6 = gr.Markdown(value='test',visible=False)

        check_box_q6.select(fn.q6_checkbox_fn,
                            inputs=[check_box_q6,show_df_q6],
                            outputs=[show_df_q6_after,public_num,private_num]) 
        submit_btm_q6.click(fn.q6_btm_fn,inputs=[check_box_q6],outputs=[ans_pic_q6,ans_word_q6,correct_md,submit_btm_q6,show_df_q6_after,show_df_q6,check_box_q6,public_num,private_num])
        
        with gr.Tab(label='問題七'):
            gr.Markdown("""
                        ### 問題七  
                        在原始的dataframe中，有一欄叫做['縣市名稱']的column，同時我有一份各縣市對應台灣地區的dictionary。  
                        我想使用這個dictionary去映射新增一個欄位叫做['地區']，最後存成新的CSV檔案，並命名為new_data.csv  
                        ```python
                        import pandas  
                        file_path = 'data.csv'  
                        data = pandas.read_csv(file_path)  
                        region_mapping = {'臺北市':'北部','新北市':'北部','基隆市':'北部','新竹市':'北部','桃園市':'北部','新竹縣':'北部',  
                                        '宜蘭縣':'北部','臺中市':'中部','苗栗縣':'中部','彰化縣':'中部','南投縣':'中部','雲林縣':'中部','高雄市':'南部',  
                                        '臺南市':'南部','嘉義市':'南部','嘉義縣':'南部','屏東縣':'南部','澎湖縣':'南部','花蓮縣':'東部','臺東縣':'東部',  
                                        '金門縣':'福建省'}  
                        ...  
                        ```
                        """)
            with gr.Row():
                with gr.Column(scale=5):
                    df1_q7 = gr.Dataframe(value=fn.q7_data1_fn(),visible=True,label='原始數據',height=400,interactive=False)
                with gr.Column(scale=1):
                    df2_q7 = gr.Dataframe(value=fn.q7_data2_fn(),visible=True,label='mapping數據',height=400,interactive=False)
            choices_q7_1 = ["data.to_csv('new_data.csv',encoding='utf-8-sig')",
                        "pandas.to_csv('new_data.csv',encoding='utf-8-sig')",
                        "pandas.csv('new_data.csv',encoding='utf-8-sig')",
                        "data.csv('new_data.csv',encoding='utf-8-sig')",
                        ]
            random.shuffle(choices_q7_1)
            markdown_q7 = gr.Markdown("```data['地區'] = data['X'].map(region_mapping)```",visible=True)
            check_box_q7 = gr.Radio(choices=fn.q7_read_column(),label='創建["地區"]欄,將要映射的欄位填入X',value=False)
            show_df_q7 = gr.Dataframe(visible=False)
            check_box2_q7 = gr.Radio(choices=choices_q7_1,label='將資料存為新的csv檔',value=False,visible=False)
            error_text2_q7 = gr.Textbox(visible=False)
            file_q7 = gr.File(visible=False)
            submit_btm_q7 = gr.Button(value='Submit',variant='primary',visible=True)
            with gr.Row():
                with gr.Column(scale=1):
                    ans_pic_q7 = gr.Image(visible=False)
                with gr.Column(scale=2):
                    ans_word_q7 = gr.Markdown(value='test',visible=False)
            dl_btm_q7 = gr.DownloadButton(label='Download new_data.csv',visible=False)
        check_box_q7.select(fn.q7_checkbox_fn,inputs=[check_box_q7],outputs=[show_df_q7,check_box2_q7])
        check_box2_q7.select(fn.q7_checkbox2_fn,inputs=[check_box2_q7],outputs=[error_text2_q7,file_q7])
        submit_btm_q7.click(fn.q7_btm_fn,inputs=[check_box_q7,check_box2_q7],outputs=[ans_pic_q7,ans_word_q7,dl_btm_q7,show_df_q7,check_box_q7,df1_q7,df2_q7,check_box2_q7,markdown_q7,submit_btm_q7,file_q7])
        
        with gr.Tab(label='問題八'):
            gr.Markdown("""
                        ### 問題八  
                        我想用pandas求出dataframe當中各體系別的學校數量。  
                        我先透過drop_duplicates()將重複的學校名稱和體系別刪除，接著我想要用什麼函數來計算體系別的學校數量呢?
                        ```python
                        import pandas

                        df = pandas.read_csv('data.csv')
                        df = df.drop_duplicates(subset=['學校名稱', '體系別'])
                        ...  
                        ```
                        """)
            show_df_q8 = gr.Dataframe(value=fn.q8_get_dataframe(), visible=True,interactive=False)
            choices_q8 = ["df['體系別'].value_counts()","df['體系別'].sort_values()"]
            random.shuffle(choices_q8)
            check_box_q8 = gr.Radio(choices=choices_q8,label='choose the correct function',value=False)
            show_df_q8_after = gr.Dataframe(visible=False,interactive=False)
            submit_btm_q8 = gr.Button(value='Submit',variant='primary',visible=True)
            with gr.Row():
                with gr.Column(scale=1):
                    ans_pic_q8 = gr.Image(visible=False)
                with gr.Column(scale=2):
                    ans_word_q8 = gr.Markdown(visible=False)
        check_box_q8.select(fn.q8_checkbox_fn,inputs=[check_box_q8,show_df_q8],outputs=[show_df_q8_after])
        submit_btm_q8.click(fn.q8_btm_fn,inputs=[check_box_q8],outputs=[ans_pic_q8,ans_word_q8,show_df_q8,check_box_q8,show_df_q8_after,submit_btm_q8])

    # demo.launch(share=True,auth=correct)
    demo.launch()
    
if __name__ == "__main__":
    random.seed(time.time())
    main()
    
    
