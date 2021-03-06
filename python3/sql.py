

str = '''
    T1.ID,T1.INVEST_NO,T1.INVEST_AMOUNT,T1.ORG_CODE,T1.SETTLE_AMOUNT,T1.CASH_SCALE,T1.INVEST_STATUS,T1.BEGIN_TIME,T1.END_TIME,T1.CREATE_TIME,T1.UPDATE_TIME,T1.INVESTOR_TYPE,
    T2.PROD_NO, T2.INVEST_NO, T2.ID, T2.TRADE_AMOUNT, T2.TRADE_DATE, T2.TRADE_STATUS, T2.CREATE_TIME, T2.UPDATE_TIME,T2.SEGMENT1, T2.SEGMENT2,
    T3.ID, T3.PROD_NO, T3.PROD_NAME, T3.PROD_TYPE, T3.CREATOR_NO, T3.PROD_AMOUNT, T3.YEAR_IRR, T3.PROD_STATUS,T3.APPLY_DATE, T3.EFFECT_DATE, T3.DEAD_LINE, T3.TRADE_DEAD_LINE, T3.CREATE_TIME, T3.UPDATE_TIME,T3.SOURCE_NUMBER, T3.SEGMENT1, T3.SEGMENT2
    '''
    
cols = str.split(',')

sql_col = '';
for col in cols:
    col = col.strip();
    print("'%s'" % col)
    sql_col += '%s AS %s, ' % (col,col.replace('.','_'))
    
print(sql_col)