from django import template
import xlsxwriter

register = template.Library()

@register.filter
def forcounter_serialno(serial_num, page_num):
    try:
        if page_num.number == 1:
            return serial_num
        return serial_num + ((page_num.number-1)*25)
    except:
        return serial_num
    
@register.filter
def column_num_to_name(agent_id):
    try:
        return f"{xlsxwriter.utility.xl_col_to_name(agent_id)}"
    except:
        return '-'
    
@register.filter
def null_handle(data):
    if data:
        return data
    return '-'

