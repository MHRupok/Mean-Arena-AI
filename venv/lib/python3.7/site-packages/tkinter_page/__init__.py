""" 
	This is a extention of tkinter
	Any error is welcome to be pointed out 
	via 'charles.shht@gmail.com'.
"""
__version__ = '0.0.5'

import tkinter as tk
import tkinter.ttk as ttk

__all__ = ["DesktopFrame", "Page"]


class DesktopFrame():
	"""
	Traditional Desktop Application Layout

	—————————————————————————————————————————————————————————————
	|                  Quick Access Bar  (bar_frame)             |
	—————————————————————————————————————————————————————————————
	|         |                                   |              |
	|         |                                   |              |
	|         |                                   |   Attribute  |
	|         |                                   |      and     |
	| Project |                                   | Configuration|
	|  Files  |             Details Pane          |     Pane     |      
	|Navigator|                                   |              |
	|         |           (details_frame)         |              |
	|         |                                   | (attributes_frame)
	|(files_frame)                                |              |
	|         |                                   |              |
	|         |                                   |              |
	—————————————————————————————————————————————————————————————
	|                    Console and Logs Pane                   |
	|                           (logs_frame)                     |
	——————————————————————————————————————————————————————————————
	
	Attributes:
		log (bool): Whether to print the detail of running
		bar_frame (tk.Frame): Quick Access Bar
		files_frame (tk.Frame): Project Files Navigator
		details_frame (tk.Frame): Details Pane
		attributes_frame (tk.Frame): Attribute and Configuration Pane
		logs_frame (tk.Frame): Console and Logs Pane
	"""

	log = False

	def __init__(self, master=None, cnf={}, **kw):
		""" Normally software application follows a master-to-detail navigation style.
		"""

		# Get Setting
		if "log" in kw:
			self.set_log(kw['log'])

		# Base Frame Init
		if self.log:
			print("Creat base_frame and mid_frame")
		self.base_frame = tk.Frame(master)
		self.mid_frame = tk.Frame(master=self.base_frame)

		# Child Frame Configure 
		if self.log:
			print("\nGetting Child Frame:")
		for child_frame in ["bar_frame","files_frame",\
			"details_frame","attributes_frame","logs_frame"]:
			if child_frame in kw:
				exec('self.set_{}(eval(\'kw["{}"]\'))'.format(child_frame,child_frame))
			else:
				exec('self.set_{}(None)'.format(child_frame))

	def set_log(self,log=False):
		""" Set Parameter Log 
		Args:
			log (bool or int or None, optional): Whether 
				to console out the running logs 
		"""
		if log:
			self.log = True
		else:
			self.log = False

	def set_bar_frame(self,frame=None):
		""" Set Bar Frame 

		Args:
			frame (None or tk.Frame or dict, optional):
				Set bar_frame, if None, set bar frame null,
				if dict, set bar frame accroding to dict,
				if tk.Frame, assign frame to bar frame.

		Raises:
			ValueError: wrong type of frame.
		"""
		if self.log: print("\nSet bar_frame")
		if frame == None:
			# Generate a empty frame
			self.bar_frame = tk.Frame(self.base_frame)
		elif type(frame) == dict:
			# Generate frame accroding to a dict
			self.bar_frame = tk.Frame(self.base_frame,frame)
		elif type(frame) == tk.Frame:
			# Directly assign a frame
			self.bar_frame = frame
		else:
			raise ValueError("You should input None or dict or class Frame.")

	def set_files_frame(self,frame=None):
		""" Set Files Frame 

		Args:
			frame (None or tk.Frame or dict, optional):
				Set bar_frame, if None, set Files frame null,
				if dict, set Files frame accroding to dict,
				if tk.Frame, assign frame to Files frame.

		Raises:
			ValueError: wrong type of frame.
		"""
		if self.log: print("\nSet files_frame")
		if frame == None:
			# Generate a empty frame
			self.files_frame = tk.Frame(self.mid_frame)
		elif type(frame) == dict:
			# Generate frame accroding to a dict
			self.files_frame = tk.Frame(self.mid_frame,frame)
		elif type(frame) == tk.Frame:
			# Directly assign a frame
			self.files_frame = frame
		else:
			raise ValueError("You should input None or dict or class Frame.")

	def set_details_frame(self,frame=None):
		""" Set Details Frame 

		Args:
			frame (None or tk.Frame or dict, optional):
				Set bar_frame, if None, set Details frame null,
				if dict, set Details frame accroding to dict,
				if tk.Frame, assign frame to Details frame.

		Raises:
			ValueError: wrong type of frame.
		"""
		if self.log: print("\nSet details_frame")
		if frame == None:
			# Generate a empty frame
			self.details_frame = tk.Frame(self.mid_frame)
		elif type(frame) == dict:
			# Generate frame accroding to a dict
			self.details_frame = tk.Frame(self.mid_frame,frame)
		elif type(frame) == tk.Frame:
			# Directly assign a frame
			self.details_frame = frame
		else:
			raise ValueError("You should input None or dict or class Frame.")

	def set_attributes_frame(self,frame=None):
		""" Set Attributes Frame 

		Args:
			frame (None or tk.Frame or dict, optional):
				Set bar_frame, if None, set Attributes frame null,
				if dict, set Attributes frame accroding to dict,
				if tk.Frame, assign frame to Attributes frame.

		Raises:
			ValueError: wrong type of frame.
		"""
		if self.log: print("\nSet attributes_frame")
		if frame == None:
			# Generate a empty frame
			self.attributes_frame = tk.Frame(self.mid_frame)
		elif type(frame) == dict:
			# Generate frame accroding to a dict
			self.attributes_frame = tk.Frame(self.mid_frame,frame)
		elif type(frame) == tk.Frame:
			# Directly assign a frame
			self.attributes_frame = frame
		else:
			raise ValueError("You should input None or dict or class Frame.")

	def set_logs_frame(self,frame=None):
		""" Set Logs Frame 

		Args:
			frame (None or tk.Frame or dict, optional):
				Set bar_frame, if None, set Logs frame null,
				if dict, set Logs frame accroding to dict,
				if tk.Frame, assign frame to Logs frame.

		Raises:
			ValueError: wrong type of frame.
		"""
		if self.log: print("\nSet logs_frame")
		if frame == None:
			# Generate a empty frame
			self.logs_frame = tk.Frame(self.base_frame)
		elif type(frame) == dict:
			# Generate frame accroding to a dict
			self.logs_frame = tk.Frame(self.base_frame,frame)
		elif type(frame) == tk.Frame:
			# Directly assign a frame
			self.logs_frame = frame
		else:
			raise ValueError("You should input None or dict or class Frame.")

	def pack(self):
		""" Pack for DesktopFrame """
		self.base_frame.pack(fill='both',expand=1)
		self.bar_frame.pack(side='top',fill='x')
		self.mid_frame.pack(side='top',fill='x')
		self.files_frame.pack(side='left',fill='y',expand=1)
		self.details_frame.pack(side='left',fill='both',expand=1)
		self.attributes_frame.pack(side='right',fill='y',expand=1)
		self.logs_frame.pack(side='bottom',fill='x')

	def pack_forget(self):
		""" Pack forget for DesktopFrame """
		for child_frame in ["bar_frame","files_frame",\
			"details_frame","attributes_frame","logs_frame"]:
				exec('self.{}.pack_forget()'.format(child_frame)) 

	def destory():
		""" Destory for DesktopFrame """
		for child_frame in ["bar_frame","files_frame",\
			"details_frame","attributes_frame","logs_frame"]:
				exec('self.{}.destory()'.format(child_frame)) 


class SplitViewFrame():
	""" Thisinheritsthe master-to-detail interface from desktop UI, 
	where changes in the primary view (the master) drive changes in a 
	secondary view (the detail).

	——————————————————————————————————————————————————————————————
	|Back Content Edit|                                          |
	|—————————————————|                                          |
	|                 |                                          |
	|      Item1      |                                          |
	|—————————————————|                                          |
	|                 |                                          |
	|      Item2      |               Details Pane               |
	|—————————————————|                                          |
	|                 |              (details_frame)             |
	|      Item3      |                                          |
	|—————————————————|                                          |
	|                 |                                          |
	|      Item4      |                                          |
	|—————————————————|                                          |
	|                 |                                          |
	|      Itemn      |                                          |
	——————————————————————————————————————————————————————————————
	"""

	log = False

	def __init__(self, master=None, cnf={}, **kw):
		""" Normally software application follows a master-to-detail navigation style.
		"""
		# Get Setting
		if "log" in kw:
			self.set_log(kw['log'])

	def set_log(self,log=False):
		""" Set Parameter Log 
		Args:
			log (bool or int or None, optional): Whether 
				to console out the running logs 
		"""
		if log:
			self.log = True
		else:
			self.log = False


class ScrollCanvas():
	"""
	"""
	def __init__(self, window,*args, vsb='y',**kwargs):
		""" 初始化带滚动条的组件
		参数说明:
			vsb: 'y',y方向滚动条; 'x',x方向滚动条; 'both',两个方向滚动条
		"""
		# 设置与主窗口
		self.sd = args[0]
		self.cd = args[1]
		self.window = window
		self.vsb = vsb
		# 创建控件
		self.canvas = tk.Canvas(self.window, borderwidth=0, background=self.cd['back'])          # 画布
		self.frame = tk.Frame(self.canvas, background=self.cd['back'])                           # 画布上的框架
		if self.vsb=='y' or self.vsb=='both':
			self.vsb1 = tk.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)   # 竖向滚动条
			self.canvas.configure(yscrollcommand=self.vsb1.set)
		if self.vsb=='x' or self.vsb=='both':
			self.vsb2 = tk.Scrollbar(self.window, orient="horizontal", command=self.canvas.xview) # 横向滚动条
			self.canvas.configure(xscrollcommand=self.vsb2.set)
		
	def _onFrameConfigure(self):
	    '''Reset the scroll region to encompass the inner frame'''
	    self.canvas.configure(scrollregion=self.canvas.bbox("all"))

	def fill_test(self):
		""" 测试填充效果 """
		for row in range(30):
			items = [['Normal Info','DataBase Info','Remind Info'],\
				['普通信息','数据库信息','提示信息']]
			test_label = FunctionalBlock(self.frame,['Info Type','信息类型'],\
				self.sd,self.cd,items=items[self.sd['language_id']],reduce_=2)
			test_label.pack()

	def pack(self):
		""" 安放控件 """ 
		self.canvas.pack(side="right", fill="both", expand=True)
		if self.vsb=='x' or self.vsb=='both':
			self.vsb2.pack(side='top',fill="x")
		if self.vsb=='y' or self.vsb=='both':
			self.vsb1.pack(side="right", fill="y")
		self.canvas.create_window((0,0),window=self.frame, anchor="nw")
		self.frame.bind("<Configure>", lambda event, canvas=self.canvas: self._onFrameConfigure())

	def pack_forget(self):
		""" 隐藏控件 """
		self.canvas.pack_forget()
		if self.vsb=='x' or self.vsb=='both':
			self.vsb2.pack_forget()
		if self.vsb=='y' or self.vsb=='both':
			self.vsb1.pack_forget()

	def destroy(self):
		""" 摧毁控件 """
		self.canvas.destroy()
		if self.vsb=='x' or self.vsb=='both':
			self.vsb2.destroy()
		if self.vsb=='y' or self.vsb=='both':
			self.vsb1.destroy()


class FunctionalBlock():
	""" Components Tip and Components pair
	for example, a combobox with combobox name,
	an extry with extry content, etc.
	"""
	'''
	def __init__(self,master,text,*args,items=[''],locked=True,kind='select',current=0,reduce_=0,key=None):
		# 设置与主窗口
		self.sd = args[0]
		self.cd = args[1]
		self.master = master
		self.kind = kind
		self.key = key
		# 创建内容
		# 创建 - 框架
		self.frame = tk.Frame(self.window,bg=self.cd['back'],width=self.sd['rwidth'])
		# 创建 - 提示标语
		if type(text) == list:
			text = text[self.sd['language_id']]
		self.label = tk.Label(self.frame,text=text, width=int(self.sd['rletter']*2/5)-reduce_,\
			fg=self.cd['front'],bg=self.cd['back'],font=(self.sd['font'],self.sd['size']))
		# 创建 - 复选框类型
		if self.kind == 'select':
			self.combobox = ttk.Combobox(self.frame, width=int(self.sd['rletter']*3/5-1),font=(self.sd['font'],self.sd['size']))
			self.combobox['values'] = (items) # 设置下拉列表的值
			self.combobox.current(current)    # 设置下拉列表默认显示的值
			if locked: self.combobox.configure(state="readonly") # 不可编辑
		# 创建 - 输入框类型
		elif self.kind == 'entry':
		    self.entry = tk.Entry(self.frame,bg=self.cd['back'],fg=self.cd['front'],\
		    	font=(self.sd['font'],self.sd['size']),width=int(self.sd['rletter']*3/5))

	def pack(self):
		""" 安放基本控件 """
		self.frame.pack()
		if self.kind == 'select':
			self.combobox.pack(side='right')
		elif self.kind == 'entry':
			self.entry.pack(side='right')
		self.label.pack(side='right')

	def pack_forget(self):
		""" 隐藏基本控件 """
		self.frame.pack_forget()
		if self.kind == 'select':
			self.combobox.pack_forget()
		elif self.kind == 'entry':
			self.entry.pack_forget()
		self.label.pack_forget()

	def destroy(self):
		""" 销毁基本控件 """
		self.frame.destroy()
		if self.kind == 'select':
			self.combobox.destroy()
		elif self.kind == 'entry':
			self.entry.destroy()
		self.label.destroy()

	def bind(self,str_,fun_):
		""" 复选框的bind """
		self.combobox.bind(str_,fun_)

	def current(self,x=None):
		""" 复选框的current """
		return self.combobox.current(x)

	def set_value(self,x):
		""" 复选框的[value] """
		self.combobox['values'] = x

	def get_key_value_pair(self):
		""" 获取键值对 """
		if self.kind == 'entry':
			return {self.key:eval(self.entry.get())}
		else:
			return {self.key:eval(self.combobox.get())}
	'''


def page_connect(father, child, page_number,text,master=None,widget=None,flavor=None,command=None):
	""" Connect two pages with Tree type
	"""
	# validation
	if type(flavor) != dict and flavor!=None:
		print(flavor)

		raise ValueError("`flavor` should be 'dict'")
	if master == None and widget == None:
		raise ValueError("`master` or `widget` should set at least one!")

	# introduce father and child
	child.set_back(father)
	father.set_child_page(child,place=len(father.child_page))

	# define jumping function
	#def to_child_func():
	#	father.pack_forget()
	#	father.child_page[page_number].pack()

	# define jumping function 2.0
	def to_child_func():
		if(command!=None):
			command()
		father.pack_forget()
		father.child_page[page_number].pack()

	# Audo Generate Fliping Button
	if widget == None:
		widget = tk.Button(master,text=text,command=to_child_func)
		if flavor!=None:
			widget.configure(flavor)

	# load Button
	elif type(widget) == tk.Button:
		widget.configure(command=to_child_func)
		if flavor!=None:
			widget.configure(flavor)

	elif type(widget) == tk.Entry:
		widget.configure(command=to_child_func)
	# ...

	else:
		raise('Invalid type of widget')

	father.add_component(widget)


class Page():
	"""
	Pages like book

	If use "combobox" type, the structure is like this:
	main - branch 1 - branch 1.1 - ...
	    |           |-branch 1.2
	    |           |-...
	    |           |-branch 1.x
	    |
	    |- branch 2 - branch 2.1
	    |           |-branch 2.2
	    |...        |-...
	    |           |-branch 2.y
	    |
	    |- branch n -...
	Each end point of the tree has the certain functional
	components that added by you. Be careful that, for example
	if you pack branch 1.1, you also pack branch 1 and main at
	the same time.
	(See the example 1 for Combobox Flipway Page)

	If use "Tree" type, the structure is not change, but this 
	more like flip book operation - you would not see the last page
	when you flip the next page.

	Of cause, if flip == None, the page does not has a child page.
	"""

	log = False
	flip = None
	back = None
	front = None
	current = -1
	show_child = False
	pack_way = None

	def __init__(self, master, cnf={}, **kw):
		""" Create a Page
		Page can have 'components' and 'child pages'.
		We can set a 'combobox' to flip child pages.
		"""

		# Get master
		self.master = master

		# Get Setting
		if "log" in kw:
			self.set_log(kw['log'])

		# Init page mumber etc.
		self.page_member = []
		self.child_page = []
		self.child_page_name = []

		# Get Child Pages 
		if "child_page" in kw:
			self.set_child_page(kw['child_page'],refresh=False)

		# Get Child Pages names
		if "child_page_name" in kw:
			self.set_child_page_name(kw['child_page_name'],auto=True,mode='RESET',refresh=False)
		else:
			self.set_child_page_name(auto=True,mode='RESET',refresh=False)

		# Genrate Page Flipping type
		if "flip" in kw:
			self.set_flip(kw['flip'],init=True)

		# Get page back to
		if "back" in kw:
			self.set_back(kw["back"])

		# Set current child page
		if "current" in kw:
			self.set_current(kw["current"])

		# wheather auto show child page
		if "show_child" in kw:
			self.set_show_child(kw["show_child"])

		# whether to pack a page
		if "pack_way" in kw:
			self.set_pack_way(kw["pack_way"])

	def set_log(self,log=False):
		""" Set Parameter Log 
		Args:
			log (bool or int or None, optional): Whether 
				to console out the running logs 
		"""
		if log:
			self.log = True
		else:
			self.log = False

	def set_flip(self,flip=None,init=False):
		""" Set Flip Ways

		Args:
			flip (str or None, optional): flip way - should be 'Combobox' or 'Tree',
				if none, use the saved option
			init (bool, optional): whether to init

		Raises:
			ValueError: wrong type of parameters
		"""
		if flip==None and self.flip==None:
			return False
		if type(init) != bool:
			raise ValueError("`init` should be bool")

		if flip == 'Combobox' or (flip == None and self.flip=='Combobox'):
			self.flip = 'Combobox'
			if init == True:
				self.flip_combobox = ttk.Combobox(self.master)
			self.flip_combobox['values'] = self.child_page_name
			self.flip_combobox.bind("<<ComboboxSelected>>",\
				self.current_set)

		elif flip == 'Tree' or (flip == None and self.flip=='Tree'):
			self.flip = 'Tree'
			if init == True:
				self.flip_button = tk.Button(self.master,text='Back',command=self.back_func)
				self.flip_title = tk.Label(self.master)

		else:
			raise ValueError("`flip` should be 'Combobox' or 'Tree'")

	def set_child_page(self,child_page,name=None,mode='ADD',
		place=0,refresh=True):
		""" Set child pages 

		You can whether input a page list or
		add into a certain place (like append)

		Args:
			child_page (list or Page list): child page
			name (str): name to the child page
			mode (str, optional): 'ADD' or 'RESET'
			place (int, optional): if mode is add, select place to insert page
			refresh (bool,  optional): whether refresh the flip combobox

		Raises:
			ValueError: wrong type of parameters
		"""
		# Valid
		if type(refresh) != bool:
			raise ValueError("`refresh` should be bool")
		if type(place) != int:
			raise ValueError("`place` should be int")
		if(len(self.child_page)<place):
			raise ValueError("`place` is too big")
		if type(child_page) == Page:
			child_page = [child_page]
		else:
			if type(child_page)!=list:
				raise ValueError("`child_page` should be Page or Page List")
			for item in child_page:
				if type(item) != Page:
					raise ValueError("`child_page` should be Page or Page List")

		# Construct new pages list
		if self.log:
			print("Constructing child_page list...")
		
		# Add or Insert child pages
		if mode == 'ADD':
			if self.log:
				print("Add child pages")
			self.child_page = self.child_page[:place]+\
				child_page + self.child_page[place:]
			self.set_child_page_name(name,place=place,auto=True,refresh=refresh)
			
		elif mode == 'RESET':
			if self.log:
				print("Insert child pages")
			self.child_page = child_page
			self.set_child_page_name(name,place=place,auto=True,refresh=refresh)

		else:
			raise ValueError("`mode` should be 'ADD' or 'RESET'")

	def set_child_page_name(self,child_page_name=None,auto=False,
		mode="ADD",place=0,refresh=True):
		""" Set child pages names

		You can whether input a str list or
		add into a certain place (like append)

		Args:
			child_page_name (str or str list or None, optional): child page name
			auto (bool, optional): If auto, the page name is the array subscript
			mode (str, optional): 'ADD' or 'RESET'
			place (int, optional): if mode is add, select place to insert name
			refresh (bool,  optional): whether refresh the flip combobox

		Raises:
			ValueError: wrong type of parameters
		"""
		# Valid
		if type(refresh) != bool:
			raise ValueError("`refresh` should be bool")
		if type(place) != int:
			raise ValueError("`place` should be int")
		if type(auto) != bool:
			raise ValueError("`auto` should be bool")
		if len(self.child_page_name)<place and auto == False:
			raise ValueError("`place` is too big")
		if len(self.child_page)<len(self.child_page_name):
			raise ValueError("`child_page_name` is too long")
		if type(child_page_name) == str:
			child_page_name = [child_page_name]
		elif child_page_name==None:
			child_page_name = []
		else:
			if type(child_page_name)!=list:
				raise ValueError("`child_page_name` should be str or str list")
			for item in child_page_name:
				if type(item) != str:
					raise ValueError("`child_page_name` should be str or str list")

		# Construct new pages list
		if self.log:
			print("Constructing child_page_name list...")
		
		# Add or Insert child pages
		if mode == 'ADD':
			if self.log:
				print("Add child pages")
			if len(self.child_page_name)+len(child_page_name) == len(self.child_page):
				self.child_page_name = self.child_page_name[:place]+\
					child_page_name + self.child_page_name[place:]
			elif auto == True:
				if self.log:
					print("Not enough name - set 0 to n y default")
				self.child_page_name = self.child_page_name[:place]+\
					list(range(len(self.child_page)-len(self.child_page_name)))\
					+ self.child_page_name[place:]
			else:
				if self.log:
					print('self.child_page: ',len(self.child_page))
					print('child_page_name: ',len(child_page_name))
					print('self.child_page_name: ',len(self.child_page_name))
				raise ValueError("`child_page_name` dose not have valid length")
			
		elif mode == 'RESET':
			if self.log:
				print("Insert child pages")

			if len(child_page_name)<len(self.child_page):
				if auto:
					if self.log:
						print("Not enough name - set 0 to n y default")
					self.child_page_name = list(range(len(self.child_page)))
				else:
					raise ValueError("`child_page_name` dose not have valid length")
			else:
				self.child_page_name = child_page_name

		else:
			raise ValueError("`mode` should be 'ADD' or 'RESET'")

		if refresh:
			self.set_flip()

	def set_back(self,back):
		""" Set back to page"""
		if type(back) != Page:
			raise ValueError("`back` should be Page")

		self.back = back

	def back_func(self):
		""" Back function
		"""
		# clear child page
		#self.destroy()
		self.pack_forget()
		# pack father page
		self.back.pack()

	def set_current(self,current):
		""" Set Current"""
		if type(current) != int:
			raise ValueError("`current` should be int")
		if self.log == True:
			print('set current = ',current)

		self.current = current

	def set_show_child(self,show_child):
		""" Set show_child"""
		if type(show_child) != bool:
			raise ValueError("`show_child` should be bool")
		if self.log == True:
			print('set if show child = ',show_child)

		self.show_child = show_child

	def set_pack_way(self,pack_way):
		""" pack_way is a function that define the way
		a page packed"""
		self.pack_way = pack_way

	def current_set(self,event=None,new_page=None):
		""" change child page """
		# Get new page number
		if self.flip == 'Combobox':
			if new_page == None:
				new_page = self.flip_combobox.current()
			elif type(new_page) == int:
				pass
			else:
				return False
		elif self.flip == 'Tree':
			pass

		# Check if need flip page
		if self.current == new_page:
			return False

		# Flip page
		if self.current != -1:
			self.child_page[self.current].pack_forget()
		if type(new_page)!=int:
			return False
		self.child_page[new_page].pack()
		self.current = new_page

	def pack(self,auto=True,show_child=False):
		# pack components and flip component
		# Use user defined pack function
		if self.pack_way != None:
			self.pack_way()
		# pack components
		else:
			if self.flip == 'Combobox':
				for item in self.page_member:
					item.pack()
				if auto == True:
					self.pack_combobox()
				# pack child page - only combobox
				if (show_child or self.show_child) and self.current!=-1:
					self.child_page[self.current].pack()
			elif self.flip == 'Tree':
				if auto == True:
					self.pack_tree()
				for item in self.page_member:
					item.pack()
			else:
				raise ValueError("Unverified flipway")

	def add_component(self,item):
		""" Add Component
		"""
		self.page_member.append(item)

	def pack_combobox(self):
		if self.flip == "Combobox":
			self.flip_combobox.pack()

	def pack_tree(self):
		if self.flip == 'Tree' and self.back!=None:
			self.flip_button.pack()

	def pack_forget(self):
		for item in self.child_page:
			item.pack_forget()
		for item in self.page_member:
			item.pack_forget()
		if self.flip == 'Tree':
			self.flip_button.pack_forget()
			self.flip_title.pack_forget()

	def destroy(self):
		for item in self.child_page:
			item.destroy()
		for item in self.page_member:
			item.destroy()
		if self.flip == 'Tree':
			self.flip_button.destroy()
			self.flip_title.destroy()
		self.child_page.clear()
		self.page_member.clear()

