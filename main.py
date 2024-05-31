#新增加了一些备注信息

from PySide6.QtCore import Qt,QDate,QUrl
from PySide6.QtWidgets import (QApplication,
                               QWidget,
                               QFileDialog,
                               QVBoxLayout,
                               QMessageBox,
                               QListView,
                               QCheckBox)
from PySide6.QtGui import (QStandardItemModel,
                           QStandardItem,
                           QIcon) 
from Ui_mainwidget import Ui_Form
from Ui_filterwidget import Ui_widget
import pandas as pd
from PySide6.QtSql import QSqlDatabase,QSqlQueryModel,QSqlQuery,QSqlTableModel
import os
import json
from sqlalchemy import create_engine,text
import plotly
import plotly.graph_objects as go
import plotly.io as pio
from plotly.io import to_image
from plotly.offline import plot
from Ui_importconfig import Ui_import_Form

class MainWidget(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        os.chdir(os.path.dirname(__file__))
        self.bind()
        self.subwindows_list()
        self.init_database()
        self.set_icon()
    def set_icon(self):
        self.setWindowIcon(QIcon('ico/xm64.ico'))
        self.filter_btn.setIcon(QIcon('ico/filter.ico'))
        self.import_config_btn.setIcon(QIcon('ico/config.ico'))
    def bind(self):
        self.datasource_btn.clicked.connect(self.choose_data)
        self.select_type_comboBox.currentIndexChanged.connect(self.get_args)
        self.sort_comboBox.currentIndexChanged.connect(self.get_args)
        self.chart_type_comboBox.currentIndexChanged.connect(self.get_args)
        self.draw_chart_btn.clicked.connect(self.draw_chart)
        self.save_chart_btn.clicked.connect(self.save_chart)
        self.filter_btn.clicked.connect(self.filter_window_show)
        self.update_title_lineEdit.textChanged.connect(self.update_title)
        self.import_config_btn.clicked.connect(self.import_config_window_show)
    def subwindows_list(self):
        self.filter_window = None
        self.subwindows_list = []
    def filter_window_show(self):
        self.filter_window = FilterWindow(self)
        self.filter_window.show()
        self.subwindows_list.append(self.filter_window)
    def import_config_window_show(self):
        self.import_config_window = ImportConfigWindow(self)
        self.import_config_window.show()
        self.subwindows_list.append(self.import_config_window)
    def closeEvent(self,event):
        #若有子窗口打开全部关闭                
        for child in self.subwindows_list:
            child.close()
    
    def init_database(self):
        self.db_name = 'xm_database.db'
        if not QSqlDatabase.contains('qt_sql_default_connection'):
            self.db = QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName(self.db_name)
            self.datasource_btn.setIcon(QIcon('./ico/database_connected.ico'))
            if not self.db.open():
                self.datasource_btn.setIcon(QIcon('./ico/database_disconnected.ico'))
                QMessageBox.critical(self,'错误','没有检测到有效的数据库连接,请联系管理员')
        self.engine = create_engine(f'sqlite:///{self.db_name}') 
        self.model = QSqlQueryModel()
        self.model.setQuery('SELECT * FROM sales_table')     
        
    def choose_data(self):   
        with open('config.json','r') as f:
            self.config_dict = json.load(f)
        self.depts_map = self.config_dict['部门名称']
        self.date_map = self.config_dict['入账日期']
        self.employees_map = self.config_dict['营业员名称']
        self.goods_map = self.config_dict['商品名称']  
        self.sales_map = self.config_dict['销售收入']       
        file_path,_ = QFileDialog.getOpenFileName(self,'选择数据文件',
                                                './python/projects/',
                                                '文件(*.xlsx *.xls *.csv)'
                                                )
        if not file_path:
            return
        if (file_path.lower().endswith(('.xlsx')) or
            file_path.lower().endswith('.xls')):
            self.df = pd.read_excel(file_path)
        elif file_path.lower().endswith(('.csv')):
            self.df = pd.read_csv(file_path)
        else:
            QMessageBox.warning(self,'错误','不支持的文件格式,请选择xlsx,xls,csv格式文件')
        if self.depts_map in self.df.columns:  
            self.df.rename(columns={self.depts_map: '部门名称'}, inplace=True) 
        if self.date_map in self.df.columns:  
            self.df.rename(columns={self.date_map: '入账日期'}, inplace=True) 
        if self.employees_map in self.df.columns:
            self.df.rename(columns={self.employees_map: '营业员名称'}, inplace=True)
        if self.goods_map in self.df.columns:
            self.df.rename(columns={self.goods_map: '商品名称'}, inplace=True)
        if self.sales_map in self.df.columns:
            self.df.rename(columns={self.sales_map: '销售收入'}, inplace=True)

        self.df['部门名称'] = self.df['部门名称'].str.split('锁').str[-1]
        self.df['营业员名称'] = self.df['营业员名称'].str.strip()        

        self.df.to_sql('sales_table',self.engine,if_exists='replace',index=False)
    def save_show_html(self,fig):
        html_content = pio.to_html(fig, include_plotlyjs=False, full_html=False)  # 注意这里将 include_plotlyjs 设置为 False  
        with open('sales_chart.html', 'w', encoding='utf-8') as f:  
            f.write("""  
            <!DOCTYPE html>  
            <html>  
            <head>  
                <script src="plotly-2.32.0.min.js"></script>  <!-- 引用 Plotly.js CDN -->  
            </head>  
            <body>  
                {}  
            </body>  
            </html>  
            """.format(html_content)) 
        # 获取当前脚本的目录（或者你的应用程序的目录）  
        script_dir = os.path.dirname(os.path.abspath(__file__))  
        
        # 构建相对于脚本目录的 HTML 文件路径  
        html_path = os.path.join(script_dir, 'sales_chart.html') 
        url = QUrl.fromLocalFile(html_path) 
        self.show_plot_webEngineView.load(url)   
    def get_args(self):
        self.report_type_index = self.select_type_comboBox.currentIndex()
        self.data_sort_index = self.sort_comboBox.currentIndex()
        self.chart_type_index = self.chart_type_comboBox.currentIndex()
        if self.report_type_index == 3:
            self.sort_comboBox.setEnabled(False)
            self.chart_type_comboBox.setCurrentIndex(2)
            if self.chart_type_index != 2:
                QMessageBox.warning(self,'操作提醒','本图形不适用于走势图,请使用折线图')
        else:
            self.sort_comboBox.setEnabled(True)
    def update_title(self):
        self.new_title = self.update_title_lineEdit.text()
        if self.new_title:
            self.fig.update_layout(title = self.new_title)
            self.save_show_html(self.fig)
    def common_layout_config(self):  
    # 公共配置    
        return {    
            'font': dict(family="SimHei", size=12),    
            'xaxis': dict(tickangle=45, showgrid=True, gridcolor='lightgray', gridwidth=1),    
            'yaxis': dict(showgrid=True, gridcolor='lightgray', gridwidth=1),    
            'plot_bgcolor': 'white'    
        }  
    def create_bar_chart(self,x, y, v,title, x_title, y_title):    
        fig = go.Figure(data=[go.Bar(x=x, y=y, orientation=v,text=[f'{round(val, 2)}' for val in y], textposition='auto', marker_color='blue')])    
        common_cfg = self.common_layout_config()  
        fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title, **common_cfg)    
        return fig    
    def create_barh_chart(self,x, y,title, x_title, y_title):    
        fig = go.Figure(data=[go.Bar(y=x, x=y, orientation='h',text=[f'{round(val, 2)}' for val in y], textposition='auto', marker_color='blue')])    
        common_cfg = self.common_layout_config()  
        fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title, **common_cfg)    
        return fig    
    def create_pie_chart(self,labels, values, title):    
        colors = plotly.colors.DEFAULT_PLOTLY_COLORS    
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', insidetextorientation='radial', marker_colors=colors)])    
        common_cfg = self.common_layout_config()  
        fig.update_layout(title=title, width=1000, height=700,**common_cfg)    
        return fig  
        
    def create_line_chart(self,x, y, mode,title, x_title, y_title): 
        common_cfg = self.common_layout_config() 
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode=mode))  
        fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title, **common_cfg)  
        return fig  
    def check_conditions(self):
        with open('config.json','r') as f:
            config_dict = json.load(f)
        selected_departments = config_dict['selected_departments']
        selected_employees = config_dict['selected_employees']
        selected_goods = config_dict['selected_goods']
        start_date = config_dict['start_date']
        end_date = config_dict['end_date']
        conditions = [] 
        #检查销售日期
        if start_date and end_date:
            conditions.append(f"入账日期 BETWEEN '{start_date}' AND '{end_date}'")
        # 检查选中的部门  
        if selected_departments:  
            selected_departments_text = ','.join(f"'{i}'" for i in selected_departments)  
            conditions.append(f"部门名称 IN ({selected_departments_text})")  
        # 检查选中的员工  
        if selected_employees:  
            selected_employees_text = ','.join(f"'{i}'" for i in selected_employees)  
            conditions.append(f"营业员名称 IN ({selected_employees_text})")  
        # 检查选中的商品
        if selected_goods:
            selected_goods_text = ','.join(f"'{i}'" for i in selected_goods)
            conditions.append(f"商品名称 IN ({selected_goods_text})")
        return conditions
        
    def draw_chart(self):
        conditions = self.check_conditions()
        if self.report_type_index == 1:
            query_text = f"SELECT 部门名称,SUM(销售收入) AS 销售收入 FROM sales_table"  
            # 如果存在条件，则添加到查询中  
            if conditions:  
                query_text += " WHERE " + " AND ".join(conditions) 
                query_text += "GROUP BY 部门名称" 
            store_sales_sum = pd.read_sql_query(query_text,self.engine)
            
            if self.chart_type_index != 1:
                if self.data_sort_index <= 1:
                    store_sales_sum = store_sales_sum.sort_values(by='销售收入')
                elif self.data_sort_index == 2 or self.data_sort_index == 0:
                    store_sales_sum = store_sales_sum.sort_values(by='销售收入',ascending=False)
          
            x = store_sales_sum['部门名称']
            y = store_sales_sum['销售收入']/10000
            if self.chart_type_index == 0:  
                self.fig = self.create_bar_chart(x, y, 'v','XX连锁各店销售额', '部门名称', '销售收入(单位:万元)')  
            elif self.chart_type_index == 1:  
                self.fig = self.create_pie_chart(store_sales_sum['部门名称'], store_sales_sum['销售收入'], 'XX连锁各店销售额占比')  
            elif self.chart_type_index == 2:  
                self.fig = self.create_line_chart(x, y,'lines+markers', 'XX连锁各店销售额', '部门名称', '销售收入(单位:万元)')  
            elif self.chart_type_index == 3:
                # 定义销售收入的分箱边界  
                bins = [0, 200000, 400000, 600000, 800000, 1000000, 1200000, 1400000, float('inf')]  
                bin_labels = ['<20万', '20-40万', '40-60万', '60-80万', '80-100万', '100-120万', '120-140万', '>=140万']  
                
                # 使用pandas的cut函数对销售收入进行分箱，并计算每个分箱中的门店数量  
                sales_bins = pd.cut(store_sales_sum['销售收入'], bins=bins, labels=bin_labels)  
                sales_bin_counts = sales_bins.value_counts().sort_index()  
                
                # 提取分箱标签和对应的门店数量  
                x = sales_bin_counts.index.tolist()  
                y = sales_bin_counts.values.tolist()  
                self.fig = self.create_bar_chart(x,y,'v','门店数量按销售收入区间分布','销售收入区间','门店数量')  
            elif self.chart_type_index == 4:#条形图
                self.fig = self.create_barh_chart(x, y, 'XX连锁各店销售额', '销售收入(单位:万元)','部门名称')  
            elif self.chart_type_index == 5:#散点图
                self.fig = self.create_line_chart(x,y,'markers','XX连锁店各店销售额','部门名称','销售收入(单位:万元)')
            self.save_show_html(self.fig)
                
        if self.report_type_index == 2:
            query_text = f"SELECT 营业员名称,SUM(销售收入) AS 销售收入 FROM sales_table"  
            # 如果存在条件，则添加到查询中  
            if conditions:  
                query_text += " WHERE " + " AND ".join(conditions) 
                query_text += "GROUP BY 营业员名称"
            
            employee_sales_sum = pd.read_sql_query(query_text,self.engine)
            employee_sales_sum = employee_sales_sum.sort_values(by='销售收入',ascending=False)
            employee_sales_sum = employee_sales_sum[employee_sales_sum['营业员名称'] != '']
            employee_sales_sum = employee_sales_sum.head(20)
            if self.chart_type_index != 1:
                if self.data_sort_index <= 1:
                    employee_sales_sum = employee_sales_sum.sort_values(by='销售收入')
                elif self.data_sort_index == 2 :
                    employee_sales_sum = employee_sales_sum.sort_values(by='销售收入',ascending=False)
            x = employee_sales_sum['营业员名称']
            y = employee_sales_sum['销售收入']/10000
            if self.chart_type_index == 0:  
                self.fig = self.create_bar_chart(x, y, 'v','XX连锁营业员销售额', '营业员名称', '销售收入(单位:万元)')  
            elif self.chart_type_index == 1:  
                self.fig = self.create_pie_chart(employee_sales_sum['营业员名称'], employee_sales_sum['销售收入'], 'XX连锁营业员销售额占比')  
            elif self.chart_type_index == 2:  
                self.fig = self.create_line_chart(x, y,'lines+markers', 'XX连锁营业员销售额', '营业员名称', '销售收入(单位:万元)')  
            elif self.chart_type_index == 3:
                # 定义销售收入的分箱边界  
                bins = [0, 1, 3, 5, 7, 9, 12, 14, float('inf')]  
                bin_labels = ['<1万', '1-3万', '3-5万', '5-7万', '7-9万', '9-12万', '12-14万', '>=14万']  
                # 使用pandas的cut函数对销售收入进行分箱，并计算每个分箱中的门店数量  
                sales_bins = pd.cut(employee_sales_sum['销售收入'], bins=bins, labels=bin_labels)  
                sales_bin_counts = sales_bins.value_counts().sort_index()  
                # 提取分箱标签和对应的门店数量  
                x = sales_bin_counts.index.tolist()  
                y = sales_bin_counts.values.tolist()  
                self.fig = self.create_bar_chart(x,y,'v','营业员数量按销售收入区间分布','销售收入区间','营业员数量')  
            elif self.chart_type_index == 4:#条形图
                self.fig = self.create_barh_chart(x, y, 'XX连锁营业员销售额', '销售收入(单位:万元)','营业员名称')  
            elif self.chart_type_index == 5:#散点图
                self.fig = self.create_line_chart(x,y,'markers','XX连锁营业员销售额','营业员名称','销售收入(单位:万元)')
            self.save_show_html(self.fig)
            
        if self.report_type_index == 3:
            query_text = f"SELECT 部门名称,入账日期,SUM(销售收入) AS 销售收入 FROM sales_table"  
            # 如果存在条件，则添加到查询中  
            if conditions:  
                query_text += " WHERE " + " AND ".join(conditions) 
                query_text += "GROUP BY 部门名称,入账日期 ORDER BY 部门名称,入账日期"
            daily_sales_sum = pd.read_sql_query(query_text,self.engine)
            daily_sales_sum['入账日期'] = pd.to_datetime(daily_sales_sum['入账日期'], format='%Y%m%d')

            if self.chart_type_index == 2:#折线图
                # 初始化一个空的列表来存储所有迹线  
                traces = []  
                # 创建一个颜色列表，用于为每个部门分配不同的颜色  
                plotly_colors = plotly.colors.DEFAULT_PLOTLY_COLORS 
                # 遍历每个部门  
                for dept, dept_data in daily_sales_sum.groupby('部门名称'):  
                    # 计算销售收入（单位：万元）  
                    y = dept_data['销售收入'] / 10000  
                    # 创建一条新的迹线  
                    trace = go.Scatter(
                    x=dept_data['入账日期'],  
                    y=y,  
                    mode='lines+markers',  
                    name=dept,  
                    line=dict(color=plotly_colors[hash(dept) % len(plotly_colors)])  # 使用部门名称的哈希值和颜色列表  
                )   
                    # 将迹线添加到列表中  
                    traces.append(trace)  
                # 创建一个图形对象  
                self.fig = go.Figure(data=traces)  
                # 设置图表的全局配置  
                self.fig.update_layout(  
                    title='XX连锁各店销售走势',  
                    xaxis_title='日期',  
                    yaxis_title='销售收入(单位:万元)',  
                    font=dict(  
                        family="SimHei",  # 中文字体  
                        size=12  # 字体大小  
                    ),  
                    xaxis=dict(  
                        tickangle=45,  # x轴标签旋转角度  
                        showgrid=True,  # 显示网格线  
                        gridcolor='lightgray',  # 网格线颜色  
                        gridwidth=1  # 网格线宽度  
                    ),  
                    yaxis=dict(  
                        showgrid=True,  # 显示网格线  
                        gridcolor='lightgray',  # 网格线颜色  
                        gridwidth=1  # 网格线宽度  
                    ),  
                    plot_bgcolor='white'  # 绘图背景色  
                )  
            
                # 显示或保存图表  
                self.save_show_html(self.fig)
            else:
                pass
        
    def save_chart(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "保存图表为图片", "", "PNG Files (*.png)")  
        if fileName:  
            # 将Plotly图表保存为图片  
            img_bytes = to_image(self.fig, format="png")  
            # 写入文件  
            with open(fileName, 'wb') as f:  
                f.write(img_bytes)  

class ImportConfigWindow(QWidget,Ui_import_Form):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        os.chdir(os.path.dirname(__file__))
        self.setWindowIcon(QIcon('ico/xm64.ico'))
        self.bind()
        self.load_config()
    def bind(self):
        self.depts_map_lineEdit.textChanged.connect(self.get_maps)
        self.date_map_lineEdit.textChanged.connect(self.get_maps)
        self.employees_map_lineEdit.textChanged.connect(self.get_maps)
        self.goods_map_lineEdit.textChanged.connect(self.get_maps)
        self.sales_map_lineEdit.textChanged.connect(self.get_maps)
    def load_config(self):
        with open('config.json','r') as f:
            self.config_dict = json.load(f)
        date_map = self.config_dict['入账日期']
        employees_map = self.config_dict['营业员名称']
        goods_map = self.config_dict['商品名称']
        sales_map = self.config_dict['销售收入']
        self.depts_map_lineEdit.setText(self.config_dict['部门名称'])
        self.date_map_lineEdit.setText(date_map)
        self.employees_map_lineEdit.setText(employees_map)
        self.goods_map_lineEdit.setText(goods_map)
        self.sales_map_lineEdit.setText(sales_map)

    def get_maps(self):
        self.date_map = self.date_map_lineEdit.text()
        self.depts_map = self.depts_map_lineEdit.text()
        self.employees_map = self.employees_map_lineEdit.text()
        self.goods_map = self.goods_map_lineEdit.text()
        self.sales_map = self.sales_map_lineEdit.text()

        self.config_dict.update({'部门名称': self.depts_map,
                                '营业员名称': self.employees_map,
                                '商品名称': self.goods_map,
                                '入账日期':self.date_map,
                                '销售收入':self.sales_map}
                                )
        with open('config.json','w') as f:
            json.dump(self.config_dict,f,ensure_ascii=False,indent=4)
        
    
class FilterWindow(QWidget,Ui_widget):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        os.chdir(os.path.dirname(__file__))
        self.bind()
        self.load_config()
        self.init_datasbase_tableView()
        self.init_listview()
        self.setWindowIcon(QIcon('ico/xm64.ico'))
        
    def load_config(self):
        try:
            with open('config.json', 'r') as f:
                self.config_dict = json.load(f)
            self.selected_departments = self.config_dict['selected_departments']
            self.selected_employees = self.config_dict['selected_employees']
            self.selected_goods = self.config_dict['selected_goods']
            self.start_date = self.config_dict['start_date']
            self.end_date = self.config_dict['end_date']
            self.depts_checked_state = self.config_dict['depts_checked_state']
            self.employees_checked_state = self.config_dict['employees_checked_state']
            self.goods_checked_state = self.config_dict['goods_checked_state']
            self.filtered_conditions_text = f'''
当前数据集筛选条件预览:

每字段选中条件最多显示前100项,不影响数据结果
==========================================>>
            
销售日期:{self.start_date}--{self.end_date}
            
部门名称:【状态:{self.depts_checked_state}】
{self.selected_departments[:100]}

员工姓名:【状态:{self.employees_checked_state}】
{self.selected_employees[:100]}

商品名称:【状态:{self.goods_checked_state}】
{self.selected_goods[:100]}
'''
            self.filtered_conditions_textEdit.setText(self.filtered_conditions_text)
   
        except Exception as e:
            print(e)
            with open('config.json', 'w') as f:
                json.dump({},f,ensure_ascii=False,indent=4)
            self.config_dict = {}
            self.selected_departments = []
            self.selected_employees = [] 
            self.selected_goods = []
            self.start_date = []
            self.end_date = []
         
    def bind(self):#绑定页面部件信号
        self.dept_lineEdit.cursorPositionChanged.connect(self.get_dept_text)
        self.employee_lineEdit.cursorPositionChanged.connect(self.get_employee_text)
        self.goods_lineEdit.cursorPositionChanged.connect(self.get_goods_text)
        self.end_dateEdit.editingFinished.connect(self.valid_dates)
        self.filter_ok_btn.clicked.connect(self.get_selected_conditions)
        self.filter_ok_btn.clicked.connect(self.update_database_tableview)
        self.filter_cancel_btn.clicked.connect(self.clear_listview)
        self.quick_date_comboBox.currentIndexChanged.connect(self.quick_dates)
        
    def init_datasbase_tableView(self):#初始化数据库视图,显示sales_talbe预览信息
        self.model = self.parent.model
         # 查询sales_table中不同部门名称的数量  
        query_fields = ['部门名称', '营业员名称', '商品名称']  
        # 将字段名映射到属性名  
        field_to_attr_mapping = {  
            '部门名称': 'depts_count',  
            '营业员名称': 'employees_count',  
            '商品名称': 'goods_count'  
        }  
  
        for field in query_fields:  
            query = QSqlQuery()  
            query.exec_(f"SELECT COUNT(DISTINCT {field}) FROM sales_table")  
            if query.next():  
                count = query.value(0)  # 获取查询结果  
                # 使用setattr和映射来设置类的属性  
                setattr(self, field_to_attr_mapping[field], count)  
 
        self.update_database_tableview()
    def init_listview(self):#初始化筛选字段的行信息列表
        self.listview_model = QStandardItemModel()
        self.filtered_data_listView.setModel(self.listview_model)
    def get_dept_text(self):#获取部门名称过滤的文本内容,即时更新列表信息
        self.dept_text = self.dept_lineEdit.text()
        self.field_name = '部门名称'
        conditions_text = self.dept_text.split(',')
        # 去除可能的空白字符并更新列表  
        conditions_text = [text.strip() for text in conditions_text if text.strip()]
        #self.selected_departments = []
        self.update_listview(self.field_name,conditions_text)
    def get_employee_text(self):#获取营业员名称过滤的文本内容,即时更新列表信息
        self.employee_text = self.employee_lineEdit.text()
        conditions_text = self.employee_text.split(',')
        # 去除可能的空白字符并更新列表  
        conditions_text = [text.strip() for text in conditions_text if text.strip()]
        self.field_name = '营业员名称'
        #self.selected_employees = []
        self.update_listview(self.field_name,conditions_text)
    def get_goods_text(self):#获取商品名称过滤的文本内容,即时更新列表信息
        self.goods_text = self.goods_lineEdit.text()
        conditions_text = self.goods_text.split(',')
        # 去除可能的空白字符并更新列表  
        conditions_text = [text.strip() for text in conditions_text if text.strip()]
        self.field_name = '商品名称'
        #self.selected_goods = []
        self.update_listview(self.field_name,conditions_text)
    def update_listview(self,field_name,conditions_text):#录入过滤条件时listview显示对应字段集合实时更新listview  
        # 清空模型数据  
        self.listview_model.clear()  
        # 如果没有条件，查询全部
        if not conditions_text:  
            self.query_str = f'''SELECT DISTINCT {field_name} FROM sales_table'''   
        else:  
        # 构建 WHERE 子句，使用 OR 连接多个 LIKE 条件  
        # 确保每个 LIKE 条件都在单词的两端使用 %，但在单词内部不使用  
            conditions = ' OR '.join(f'{field_name} LIKE :conditions_text{i}' for i in range(len(conditions_text)))  
            self.query_str = f'''SELECT DISTINCT {field_name} FROM sales_table   
                        WHERE {conditions}  
                        '''  
        query = QSqlQuery()  
        query.prepare(self.query_str)  
          
        # 绑定值，确保每个条件都只在单词的两端使用 %  
        for i, text in enumerate(conditions_text):  
            query.bindValue(f":conditions_text{i}", f'%{text}%') 
  
        if query.exec_():  
            while query.next():  
                condition_name = query.value(0)  
                text_item = QStandardItem(condition_name)  
                text_item.setCheckable(True)  
                text_item.setCheckState(Qt.Checked)  # 默认选中  
                self.listview_model.appendRow(text_item)  
                self.selected_goods.append(condition_name)  # 假设您还想保留这些选中的商品名称  
    def get_selected_conditions(self):
        if '部门名称' in self.query_str:
            self.selected_departments = []
            for row in range(self.listview_model.rowCount()):
                    item = self.listview_model.item(row,0)
                    if item.checkState() == Qt.Checked:
                        self.selected_departments.append(item.text())
            return self.selected_departments
        elif '营业员名称' in self.query_str:
            self.selected_employees = []
            for row in range(self.listview_model.rowCount()):
                item = self.listview_model.item(row,0)
                if item.checkState() == Qt.Checked:
                    self.selected_employees.append(item.text())
            return self.selected_employees
        elif '商品名称' in self.query_str:
            self.selected_goods = []
            for row in range(self.listview_model.rowCount()):
                item = self.listview_model.item(row,0)
                if item.checkState() == Qt.Checked:
                    self.selected_goods.append(item.text())
            return self.selected_goods
    def clear_listview(self):#清空筛选字段的行信息列表
        self.listview_model.clear()
    
    def get_startdate_text(self):#获取查询起始日期
        self.start_qdate = self.start_dateEdit.date()
        if self.start_qdate.isValid():
            self.start_date = f"{self.start_qdate.year()}{self.start_qdate.month():02d}{self.start_qdate.day():02d}" 

    def get_enddate_text(self):#获取查询结束日期并更新列表
        self.end_qdate = self.end_dateEdit.date()
        if self.end_qdate.isValid():
            self.end_date = f"{self.end_qdate.year()}{self.end_qdate.month():02d}{self.end_qdate.day():02d}" 
    def get_week_start_end(self,date):  
    # 一周的第一天（假设是周一）  
        start_of_week = date.addDays(-(date.dayOfWeek() - 1))  
        end_of_week = start_of_week.addDays(6)  
        return start_of_week, end_of_week  
    
    def get_month_start_end(self,date):  
        # 一月的开始  
        start_of_month = QDate(date.year(), date.month(), 1)  
        # 一月的结束（下一个月的第一天减一天）  
        end_of_month = start_of_month.addMonths(1).addDays(-1)  
        return start_of_month, end_of_month  
    
    def get_quarter_start_end(self,date):  
        # 季度的开始（月份减去月份数对3的余数，加1确保为正）  
        quarter_start_month = (date.month() - date.month() % 3 + 1) % 12 + 1  
        start_of_quarter = QDate(date.year(), quarter_start_month, 1)  
        # 季度的结束（下一个季度的第一天减一天）  
        end_of_quarter = start_of_quarter.addMonths(3).addDays(-1)  
        return start_of_quarter, end_of_quarter  
    
    def get_year_start_end(self,date):  
        # 一年的开始  
        start_of_year = QDate(date.year(), 1, 1)  
        # 一年的结束（下一年的第一天减一天）  
        end_of_year = start_of_year.addYears(1).addDays(-1)  
        return start_of_year, end_of_year 
    
    def quick_dates(self):
        today = QDate.currentDate()
        yesterday = today.addDays(-1) 
        # 上周  
        last_week_start, last_week_end = self.get_week_start_end(today.addDays(-7))  
        
        # 上月  
        last_month_start, last_month_end = self.get_month_start_end(today.addMonths(-1))  
        
        # 上季度  
        last_quarter_start, last_quarter_end = self.get_quarter_start_end(today.addMonths(-3))  
        
        # 上年  
        last_year_start, last_year_end = self.get_year_start_end(today.addYears(-1))  
        
        # 本周  
        this_week_start, this_week_end = self.get_week_start_end(today)  
        
        # 本月  
        this_month_start, this_month_end = self.get_month_start_end(today)  
        
        # 本季度  
        this_quarter_start, this_quarter_end = self.get_quarter_start_end(today)  
        
        # 本年  
        this_year_start, this_year_end = self.get_year_start_end(today)

        quick_date_index = self.quick_date_comboBox.currentIndex()
        if quick_date_index  == 1:
            self.start_dateEdit.setDate(today)
            self.end_dateEdit.setDate(today)
        elif quick_date_index == 2:
            self.start_dateEdit.setDate(yesterday)
            self.end_dateEdit.setDate(yesterday)
        elif quick_date_index == 3:
            self.start_dateEdit.setDate(last_week_start)
            self.end_dateEdit.setDate(last_week_end)
        elif quick_date_index == 4:
            self.start_dateEdit.setDate(last_month_start)
            self.end_dateEdit.setDate(last_month_end)
        elif quick_date_index == 5:
            self.start_dateEdit.setDate(last_quarter_start)
            self.end_dateEdit.setDate(last_quarter_end)
        elif quick_date_index == 6:
            self.start_dateEdit.setDate(last_year_start)
            self.end_dateEdit.setDate(last_year_end)
        elif quick_date_index == 7:
            self.start_dateEdit.setDate(this_week_start)
            self.end_dateEdit.setDate(this_week_end)
        elif quick_date_index ==8:
            self.start_dateEdit.setDate(this_month_start)
            self.end_dateEdit.setDate(this_month_end)
        elif quick_date_index == 9:
            self.start_dateEdit.setDate(this_quarter_start)
            self.end_dateEdit.setDate(this_quarter_end)
        elif quick_date_index ==10:
            self.start_dateEdit.setDate(this_year_start)
            self.end_dateEdit.setDate(this_year_end)
        self.valid_dates()
    def valid_dates(self):
        self.get_startdate_text()  
        self.get_enddate_text()  
    
        if self.end_qdate >= self.start_qdate:  
            self.config_dict.update({'start_date': self.start_date,  
                                    'end_date': self.end_date  
                                    })  
    
            with open('config.json', 'w') as f:  
                json.dump(self.config_dict, f, ensure_ascii=False, indent=4)  
    
            self.load_config()  
            self.update_database_tableview()  
        else:  
            QMessageBox.warning(self, '非法操作', '结束日期必须大于等于开始日期')  
    
    def update_database_tableview(self):
        # 初始化查询  
        query = "SELECT * FROM sales_table"  
        conditions = []  
        #检查销售日期
        if self.start_date and self.end_date:
            conditions.append(f"入账日期 BETWEEN '{self.start_date}' AND '{self.end_date}'")
        # 检查选中的部门  
        if self.selected_departments:  
            selected_departments_text = ','.join(f"'{i}'" for i in self.selected_departments)  
            conditions.append(f"部门名称 IN ({selected_departments_text})")  
    
        # 检查选中的员工  
        if self.selected_employees:  
            selected_employees_text = ','.join(f"'{i}'" for i in self.selected_employees)  
            conditions.append(f"营业员名称 IN ({selected_employees_text})")  

        # 检查选中的商品
        if self.selected_goods:
            selected_goods_text = ','.join(f"'{i}'" for i in self.selected_goods)
            conditions.append(f"商品名称 IN ({selected_goods_text})")
        # 如果存在条件，则添加到查询中  
        if conditions:  
            query += " WHERE " + " AND ".join(conditions)  

        # 准备查询并执行  
        self.model.setQuery(query)  
        self.database_tableView.setModel(self.model)  
        self.database_tableView.resizeColumnsToContents()
        if self.depts_count == len(self.selected_departments):
            self.config_dict.update({'depts_checked_state':'全部'})
        else:
            self.config_dict.update({'depts_checked_state':'部分'})
        if self.employees_count == len(self.selected_employees):
            self.config_dict.update({'employees_checked_state':'全部'})
        else:
            self.config_dict.update({'employees_checked_state':'部分'})
        if self.goods_count == len(self.selected_goods):
            self.config_dict.update({'goods_checked_state':'全部'})
        else:
            self.config_dict.update({'goods_checked_state':'部分'})
        self.config_dict.update({'selected_departments':self.selected_departments,
                                 'selected_employees':self.selected_employees,
                                 'selected_goods':self.selected_goods,
                                 'start_date':self.start_date,
                                 'end_date':self.end_date,
                                 })
        with open('config.json','w') as f:
            json.dump(self.config_dict,f,ensure_ascii=False,indent=4) 
        self.load_config()



if __name__ == '__main__':
    app = QApplication([])
    window = MainWidget()
    window.show()
    app.exec()
