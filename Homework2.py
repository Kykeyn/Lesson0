#Первый вариат. Тут результат визуально больше нравится)
Count_completed_HW = 12
Count_hours_spend = 1.5
Course_name = 'Python'
Time_per_task = (Count_hours_spend / Count_completed_HW)
print("Курс:" + Course_name + ","" всего задач:"+ str(Count_completed_HW) +", затрачено часов:"+str(Count_hours_spend)+
      ", среднее время выполнения:"+str(Time_per_task),"часа")

#Второй вариант
Count_completed_HW = 12
Count_hours_spend = 1.5
Course_name = 'Python'
Time_per_task = (Count_hours_spend / Count_completed_HW)
print("Курс:", Course_name, ",""всего задач:", Count_completed_HW ,",затрачено часов:",Count_hours_spend,
      ",среднее время выполнения:",Time_per_task,"часа")

#Ещё вариант из вашей подсказки по доп. информации
Count_completed_HW = 12
Count_hours_spend = 1.5
Course_name = 'Python'
Time_per_task = (Count_hours_spend / Count_completed_HW)
print(f"Курс:{Course_name}, всего задач:{Count_completed_HW}, затрачено часов:{Count_hours_spend},"
      f" среднее время выполнения:{Time_per_task}")
