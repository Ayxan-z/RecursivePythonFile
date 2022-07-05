start = 1
stop = 10
t = 1
import os

#

#

if t:
    with open(__file__, 'r+') as d:
        data_cnt = d.readline()
        first_space = data_cnt.rfind(' ')
        data_cnt = data_cnt[:first_space+1] + str(int(data_cnt[first_space+1:-1]) + 1) + '\n'

        all_data = d.read()
        all_data = data_cnt + all_data
        first_point = all_data.find('#')
        second_point = all_data.find('#', first_point+1)
        d.seek(0)

        if all_data.find('if', first_point, second_point+1) == -1:
            d.write(all_data[:first_point+2] + f"if {start} == stop: t = 0" + all_data[second_point-1:])

        else:
            d.write(all_data[:second_point-1] + f"\nelif {start} == stop: t = 0" + all_data[second_point-1:])

    os.system('python ' + __file__)