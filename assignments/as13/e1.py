#http://127.0.0.1:5000/prime_number/31
from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route('/prime_number/<number>', methods=['GET'])
def is_prime(number):
    try:
        num=int(number)
        def return_prime_status(n):
            if n==2:
                return True
            if n<=1 or n%2==0:
                return False
            for i in range(3, int(n**0.5)+1, 2):
                if n%i==0:
                    return False
            return True
        return jsonify({'number': num, 'is_prime': return_prime_status(num)})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400
if __name__=="__main__":
    app.run(debug=True)