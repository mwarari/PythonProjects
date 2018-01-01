try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


class ScrollBox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        # tikinter.Listbox.__init__(self, window, **kwargs) # python 2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspan=rowspan, **kwargs) # python 2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(ScrollBox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        # ScrollBox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, **kwargs)

        self.cursor = connection.cursor()
        self.table = table
        self.field = field
        self.data = []

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)
        self.data = []

    def update(self, link_field=None, link_value=None):
        if link_value:
            sql = self.sql_select + " WHERE " + link_field + "=?" + self.sql_sort
            # print(sql)  # TODO delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            # print(self.sql_select + self.sql_sort)  # TODO delete this line
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])
            self.data.append((value[1], value[0]))
