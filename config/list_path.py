# Path constants

target = './config/target_list.csv'

### ⚠️CAUTION 注意⚠️ ###
# Every strings should be in Quotation marks (", ')
# 全ての文句は引用符("または')の中にに入れること
#
# Quotation mark in strings should be with the Backslash (\)
# 文句の中に引用符が入る場合、バックスラッシュ(\)を引用符の前に書くこと
#  
# [Example 例]
# 'Scan Session using Service Generic Scan protocol in \'Reference Service\' protocol category'
# "Scan Session using Service Generic Scan protocol in 'Reference Service' protocol category"
# "Scan Session using Service Generic Scan protocol in \"Reference Service\" protocol category"

### Path Explanation パス説明###
# '.' : current directory 現在のフォルダ
# '..' : parent directory 現在のフォルダの上位フォルダ
# '/' : path division 区切り
#
# [Example 例]
# ../string_changer.py
# ./config/target_list.csv