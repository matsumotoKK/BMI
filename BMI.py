def get_BMI(whight,height):
    return (whight / height ** 2)
    
input_height = int(input('あなたの身長を入力してください(cm)：'))
input_height *= 0.01
input_whight = int(input('あなたの体重を入力してください(Kg)：'))
print('あなたのBMIは' + str(round(get_BMI(input_whight,input_height),2)) + 'です！')