from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  #return 'Hello World!'
  return render_template('index.html')


@app.route('/dohyeon')
def dohyeon():
   return '저는 무술가입니다'

@app.route('/html')
def html():
  return '<h1>태그 사용할 수 있어용!</h1>'

@app.route('/html_multiline')
def html_multiline():
  return """
  <ol>
    <li>하이하이</li>
    <li>안녕안녕</li>
  <ol>
  """

# 동적 라우팅 (Variable Routing)
@app.route('/greeting/<string:name>')
def greeting(name):
  #return f'안녕, {naem}?'
  return render_template('greeting.html', html_name=name)


# 세제곱을 돌려주는 cube 페이지 작성!
# 사용자한테 숫자값을 받아서, 세제곱한 결과를 보여주는 페이지 
@app.route('/cube/<int:number>')
def cube(number):
  #number = int(number)
  #result = str(number*number*number)
  result = number ** 3
  #return result
  return render_template('cube.html', result = result, number = number )
  #return render_template('triple.html', html_number = number)

@app.route('/movies')
def movies():
  movie_list = ['82년생 김지영', '조커', '엔드게임', '궁예']
  return render_template('movies.html', movies=movie_list)


# end of file !!!!!
# debug 모드를 활성화해서 서버 새로고침을 생략한다. 
if __name__ == '__main__':
  app.run(debug=True)
