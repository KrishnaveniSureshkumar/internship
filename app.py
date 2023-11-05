from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# First Page - Welcome
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Second Page - Voting
@app.route('/voting', methods=['GET', 'POST'])
def voting():
    if request.method == 'POST':
        return render_template('voting.html')
    return redirect('/')

# Submit Vote
@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    username = request.form['username']
    voter_id = request.form['voterId']
    selected_candidate = request.form['candidate']

    # Simulate submitting the vote to a server (replace with actual code)
    # send_vote_to_server(username, voter_id, selected_candidate)

    flash("Your voting process is successfully completed.")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
