#http://127.0.0.1:5000/prime_number/31
from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route('/prime_number/<number>', methods=['GET'])
def 素数检验(number):
    try:
        数字=int(number)
        def 返回素数状态(数字):
            if 数字==2:
                return True
            if 数字<=1 or 数字%2==0:
                return False
            for i in range(3, int(数字**0.5)+1, 2):
                if 数字%i==0:
                    return False
            return True
        return jsonify({'number': 数字, 'is_prime': 返回素数状态(数字)}) #返回JSON响应，包含数字及其素数状态
    #英语输入错误处理
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400
    #英文错误处理结束
if __name__=="__main__":
    app.run(debug=True)