import bcrypt
import random 
import string
from datetime import datetime
from flask import Flask, request, jsonify, session, redirect
from flask_bcrypt import Bcrypt
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash
from flask_mysqldb import MySQL
from cryptography.fernet import Fernet
from flask import Flask, send_file, render_template


app = Flask(__name__)
bcrypt = Bcrypt(app)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'siddhi1234'
app.config['MYSQL_DB'] = 'password_vault'

# Initialize MySQL
mysql = MySQL(app)

# Set secret key for session


app.secret_key = 'siddhi1234'


#---------------------------------------------------------------------------------------------------------------
# Endpoint for the home page
@app.route('/', methods=['GET'])
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/home_style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <title>Home Page|Parallax</title>

</head>
<body>
   <header>
    <!-- <a href="#" class="logo">Logo</a> -->
    <div class="logo">
        <img src="/static/images/logo_Gemini_Generated_Image2.jpg" class="logoincorner">
        <h2>PS<span class="danger">VAULT</span></h2>
    </div>
    <ul class="navlist">
        <li><a href="home_index.html" class="active">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#products">Features</a></li>
        <li><a href="#contact">Contact us</a></li>
       
    </ul>
   </header> 
   
   <section class="parallax-home">
        <h1 id="text1">PASSWORD SECURITY VAULT</h1>
        <p id="text2">Experience unparalleled security and convenience with our state-of-the-art password management system. </p>
   </section>

   <section class="about" id="about">
        <div class="info-box">
            <h2>About Us</h2>
            <p>
                Secure, Manage, and Update Your Passwords Effortlessly
            </p>
            <a href="/sign_up" class="btn">Join Now</a>
            
        </div>

        <div id="progress">
            <span id="progress-value">
                <i class='bx bx-chevrons-up'></i>
            </span>
        </div>
        
    </section>

    <section class="products" id="products">
        <h2>Our Features</h2>
        <div class="product-cart">
            <div class="card">
                <img src="/static/images/key images.webp">
                <div class="info">
                    <div class="price-name">
                        <h3>Generate Password</h3>
                    </div>
                
                    <a href="#" class="btn">Read more</a>
                </div>
            </div>

            <div class="card">
                <img src="/static/images/vault 1_gemini_Generated_Image.jpeg">
                <div class="info">
                    <div class="price-name">
                        <h3>Store Passwords</h3>
                    </div>
                    <a href="#" class="btn">Read more</a>
                </div>
            </div>

            <div class="card">
                <img src="/static/images/trolley-lock.jpg" alt="">
                <div class="info">
                    <div class="price-name">
                        <h3>Check Strength</h3>
                    </div>
                
                    <a href="#" class="btn">Read more</a>
                </div>
            </div>

            <div class="card">
                <img src="/static/images/emergency-contacts.jpg" alt="">
                <div class="info">
                    <div class="price-name">
                        <h3>Emergency Contacts</h3>
                    </div>
                
                    <a href="#" class="btn">Read more</a>
                </div>
            </div>
        </div>
        <br>
        <a href="#" class="more-cards">More features -></a>
    </section>

    <footer>
        <section class="contact-us" id="contact">
            
            <div class="footerContainer">
                <div class="socialIcons">
                    <a href=""><i class="fa-brands fa-facebook"></i></a>
                    <a href=""><i class="fa-brands fa-github"></i></a>
                    <a href=""><i class="fa-brands fa-twitter"></i></a>
                    <a href=""><i class="fa-brands fa-whatsapp"></i></a>
                    <a href=""><i class="fa-brands fa-instagram"></i></a>
                </div>
                <div class="footerBottom">
                    <p>Copyrights &copy;2024;  <span class="."></span></p>
                </div>
            </div>
        </section>
    </footer>
    <script src="/static/home_script.js"></script>
</body>
</html>

"""
#--------------------------------------------------------------------------------------------------

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to MySQL database
        conn = mysql.connection
        cursor = conn.cursor()

        try:
            # Insert data into users table
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            val = (username, password)
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
            return redirect('/login')
        except Exception as e:
            print("Error:", e)
            return "An error occurred while registering. Please try again."

    return (sign_up_html)

sign_up_html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/sign_up_style.css">
    <title>Login & Registration</title>
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

    <style>
        /* Add this to your existing CSS file or in a <style> tag */
        /* Responsive Styles */
        @media screen and (max-width: 768px) {
            .wrapper {
                width: 100%;
                padding: 20px;
            }

            .form-box {
                width: 100%;
            }

            .input-box {
                width: 100%;
            }

            .btn {
                width: 100%;
            }

            .info-text {
                width: 100%;
            }
        }
    </style>

</head>

<body>
    <div class="wrapper">
        <span class="bg-animate"></span>
        <span class="bg-animate2"></span>

        <div class="form-box login">
            <h2 class="animation" style="--i:0; --j:21;">Sign Up</h2>
            <form action="/sign_up" method="POST">
                <div class="input-box animation" style="--i:1; --j:22;">
                    <input type="text" name="username" required>
                    <label>Username</label>
                    <i class='bx bxs-user'></i>
                </div>
                <div class="input-box animation" style="--i:2; --j:23;">
                    <input type="password" name="password" required>
                    <label>Password</label>
                    <i class='bx bxs-lock-alt'></i>
                </div>
                <br>
                <button type="submit" class="btn animation" style="--i:3; --j:24;">Sign Up</button>
                <div class="logreg-link animation" style="--i:4; --j:25;">
                    <p>
                        Already have an account? <a href="/login">Login</a>
                    </p>
                </div>
            </form>
        </div>
        
        <div class="info-text login">
            <h2 class="animation" style="--i:0; --j:20;">Register Now!</h2>
            <p class="animation" style="--i:1; --j:21;">.</p>
        </div>
    </div>    

    <script src="/static/sign_up_script.js"></script>
</body>

</html>
"""
#--------------------------------------------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to MySQL database
        conn = mysql.connection
        cursor = conn.cursor()
        
        try:
            # Check if the username and password match
            sql = "SELECT * FROM users WHERE username = %s AND password = %s"
            val = (username, password)
            cursor.execute(sql, val)
            user = cursor.fetchone()
            cursor.close()
            
            if user:
                session['username'] = username
                return redirect('/dashboard')
            else:
                error_message = "Credentials don't match. Please try again."
                return login_html(error_message)
        except Exception as e:
            print("Error:", e)
            return "An error occurred while logging in. Please try again."
    
    return login_html()


def login_html(error_message=None):
    html = """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/login_style.css">
    <title>Login</title>
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

    <style>
        /* Add this to your existing CSS file or in a <style> tag */
        /* Responsive Styles */
        @media screen and (max-width: 768px) {
            .wrapper {
                width: 100%;
                padding: 20px;
            }

            .form-box {
                width: 100%;
            }

            .input-box {
                width: 100%;
            }

            .btn {
                width: 100%;
            }

            .info-text {
                width: 100%;
            }
            .error-message {
                color: red; /* Ensure error messages are displayed in red */
            }
        }
    </style>

</head>

<body>
    <div class="wrapper">
        <span class="bg-animate"></span>
        <span class="bg-animate2"></span>

        <div class="form-box login">
            <h2 class="animation" style="--i:0; --j:21;">Login</h2>
            <form action="/login" method="POST">
                <div class="input-box animation" style="--i:1; --j:22;">
                    <input type="text" name="username" required>
                    <label>Username</label>
                    <i class='bx bxs-user'></i>
                </div>
                <div class="input-box animation" style="--i:2; --j:23;">
                    <input type="password" name="password" required>
                    <label>Password</label>
                    <i class='bx bxs-lock-alt'></i>
                </div>
                <div class="logreg-link animation" style="--i:4; --j:25;">
                    <p>
                       <a href="/forgot_password">Forgot Password</a>
                    </p>
                </div>
                <br>
                <button type="submit" class="btn animation" style="--i:3; --j:24;">Login</button>
                <div class="logreg-link animation" style="--i:4; --j:25;">
                    <p>
                        Don't have an account? <a href="/sign_up">Sign Up</a>
                    </p>
                </div>
            </form>
            <!-- Error message will be displayed here -->
            <div class="error-message">
                """ + (f"{error_message}" if error_message else "") + """
            </div>
        </div>

        <div class="info-text login">
            <h2 class="animation" style="--i:0; --j:20;">Welcome Back!</h2>
            <p class="animation" style="--i:1; --j:21;">.</p>
        </div>
    </div>

    <script src="/static/login_script.js"></script>
</body>

</html>

    """
    return html

#---------------------------------------------------------------------------------------------------
# Endpoint for the dashboard
@app.route('/dashboard', methods=['GET'])
def dashboard():
    return """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/dashboard_style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
    <title>Responsive Dashboard Design #2 | AsmrProg</title>
</head>

<body>

    <!-- Sidebar -->
    <div class="sidebar">
        <a href="#" class="logo">
            <i class='bx bx-code-alt'></i>
            <div class="logo-name"><span>PS</span>Vault</div>
        </a>
        <ul class="side-menu">
            <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
            <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
            <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
            <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
            <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
            <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
            <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
        </ul>
        <ul class="side-menu">
            <li>
                <a href="/logout">
                    <i class='bx bx-log-out-circle'></i>
                    Logout
                </a>
            </li>
        </ul>
    </div>
    <!-- End of Sidebar -->

    <!-- Main Content -->
    <div class="content">
        <!-- Navbar -->
        <nav>
            <i class='bx bx-menu'></i>
            <form action="#">
                <div class="form-input">
                    <input type="search" placeholder="Search...">
                    <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                </div>
            </form>
            <a href="#" class="profile">
                
            </a>
        </nav>

        <!-- End of Navbar -->

        <main>
            <!-- Insights -->
            <ul class="insights">
                <li>
                    <a href="/my_vault">
                        <img src="/static/images/Digital Vault.jpg">
                        <span class="info">
                            <h3>
                                Visit Vault
                            </h3>
                        </span>
                    </a>
                </li>
                <li>
                    <a href="/strength_meter">
                        <img src="/static/images/vault 1_gemini_Generated_Image.jpeg">
                        <span class="info">
                            <h3>
                                Strength Check
                            </h3>
                        </span>
                    </a>
                </li>
                <li>
                    <a href="/password_generator">
                        <img src="/static/images/key images.webp">
                        <span class="info">
                            <h3>
                                New Key
                            </h3>
                        </span>
                    </a>
                </li>
                <li>
                    <a href="/new_entry">
                        <img src="/static/images/vault_Gemini_Generated_Image.jpeg">
                        <span class="info">
                            <h3>
                                New Entry
                            </h3>
                        </span>
                    </a>
                </li>
            </ul>
            <!-- End of Insights -->

            <div class="bottom-data">
                <div class="orders"> 
                    <div class="header">
                        <a href="#">
                            <h3>History</h3>
                        </a>
                        <i class='bx bx-search'></i>
                    </div>
                    <table>
                        <thead>
                            <tr>
                                <th>User</th>
                                <th>Order Date</th>
                                <th>Changes Done</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    
                                    <p>Siddhi Raney</p>
                                </td>
                                <td>10-05-2023</td>
                                <td><span class="status completed">UPDATED</span></td>
                            </tr>
                            <tr>
                                <td>
                                    
                                    <p>User</p>
                                </td>
                                <td>11-05-2023</td>
                                <td><span class="status pending">UPDATED</span></td>
                            </tr>
                            <tr>
                                <td>
                                    
                                    <p>Tina Naik</p>
                                </td>
                                <td>15-05-2023</td>
                                <td><span class="status process">UPDATED</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Reminders -->
                <div class="reminders">
                    <div class="header">
                        <i class='bx bx-note'></i>
                        <h3>Reminders</h3>
                        <i class='bx bx-filter'></i>
                    </div>
                    <ul class="task-list">
                        <li class="completed">
                            <div class="task-title">
                                <i class='bx bx-check-circle'></i>
                                <p class="font-color">Password was last changed Today.</p>
                            </div>
                            <i class='bx bx-dots-vertical-rounded'></i>
                        </li>
                        <li class="completed">
                            <div class="task-title">
                                <i class='bx bx-check-circle'></i>
                                <p class="font-color">Check your password strength</p>
                            </div>
                            <i class='bx bx-dots-vertical-rounded'></i>
                        </li>
                        <li class="not-completed">
                            <div class="task-title">
                                <i class='bx bx-x-circle'></i>
                                <p class="font-color">ALERT!! Update Passwords</p>
                            </div>
                            <i class='bx bx-dots-vertical-rounded'></i>
                        </li>
                    </ul>
                </div>

                <!-- End of Reminders-->

            </div>

        </main>

    </div>

    <script src="/static/dashboard_script.js"></script>
</body>

</html>
"""


#---------------------------------------------------------------------------------------------------



@app.route('/emergency_contacts', methods=['GET', 'POST'])
def emergency_contacts():
    if request.method == 'GET':
        # Serve HTML form for entering emergency contact
        return """
        <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/emergency_contacts_style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
    <title>Responsive Dashboard Design #2 | AsmrProg</title>
</head>

<body>

    <!-- Sidebar -->
    <div class="sidebar">
        <a href="#" class="logo">
            <i class='bx bx-code-alt'></i>
            <div class="logo-name"><span>PS</span>Vault</div>
        </a>
        <ul class="side-menu">
            <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
            <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
            <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
            <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
            <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
            <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
            <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
        </ul>
        <ul class="side-menu">
            <li>
                <a href="/logout">
                    <i class='bx bx-log-out-circle'></i>
                    Logout
                </a>
            </li>
        </ul>
    </div>
    <!-- End of Sidebar -->

    <!-- Main Content -->
    <div class="content">
        <!-- Navbar -->
        <nav>
            <i class='bx bx-menu'></i>
            <form action="#">
                <div class="form-input">
                    <input type="search" placeholder="Search...">
                    <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                </div>
            </form>
            <a href="#" class="profile">
                <img src="images/profile-1.jpg">
            </a>
        </nav>

        <!-- End of Navbar -->

        <main>
            <div class="header">
                <div class="left">
                    <h1>Emergency Contacts</h1>
                </div>
            </div>

            <div class="bottom-data">
                <div class="orders">
                    <div class="header">
                        <i class='bx bx-shield-plus'></i>
                        <h3>Emergency Contacts</h3>
                    </div>
                    <h3></h3>
                    <div class="details">
                        <form action="/emergency_contacts" method="POST">
                            <div class="input-box">
                                <label>Enter Username</label>
                                <input type="text" name="username" required>
                            </div>
                            <div class="input-box">
                                <label>Enter Emergency Contact</label>
                                <input type="text" name="emergency_contact" required>
                            </div>
                            <br>
                            <br>
                            <button type="submit" class="btn">Submit</button>
                        </form>
                    </div>
                </div>
            </div>
        </main>
    </div>
    <script src="emergency_contacts_script.js"></script>
</body>

</html>
"""
    elif request.method == 'POST':
        # Extract form data and process it
        username = request.form.get('username')
        emergency_contact = request.form.get('emergency_contact')

        if not username or not emergency_contact:
            return jsonify({'message': 'Username and emergency contact are required.'}), 400

        # Check if the username exists in the database
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()

        if user is None:
            cursor.close()
            return jsonify({'message': 'User not found.'}), 404

        # Update the user's emergency contact in the database
        cursor.execute('UPDATE users SET emergency_contact = %s WHERE username = %s', (emergency_contact, username))
        mysql.connection.commit()
        cursor.close()

        return redirect('/dashboard')

    
#-------------------------------------------------------------------------------------------

@app.route('/new_entry', methods=['GET', 'POST'])
def enter_passwords():
    if request.method == 'GET':
        # Serve HTML form for entering passwords
        return """
        <!DOCTYPE html>
        <html lang="en">

        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="/static/new_entry_style.css">
        <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
        <title>Responsive Dashboard Design #2 | AsmrProg</title>
        </head>

        <body>

        <!-- Sidebar -->
        <div class="sidebar">
        <a href="#" class="logo">
            <i class='bx bx-code-alt'></i>
            <div class="logo-name"><span>PS</span>Vault</div>
        </a>
        <ul class="side-menu">
           <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
            <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
            <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
            <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
            <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
            <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
            <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
        </ul>
        <ul class="side-menu">
            <li>
                <a href="#" class="logout">
                    <i class='bx bx-log-out-circle'></i>
                    Logout
                </a>
            </li>
        </ul>
    </div>
    <!-- End of Sidebar -->

    <!-- Main Content -->
    <div class="content">
        <!-- Navbar -->
        <nav>
            <i class='bx bx-menu'></i>
            <form action="#" method="POST">
                <div class="form-input">
                    <input type="search" placeholder="Search...">
                    <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                </div>
            </form>
            <a href="#" class="profile">
                <img src="images/profile-1.jpg">
            </a>
        </nav>

        <!-- End of Navbar -->

        <main>
            <div class="header">
                <div class="left">
                    <h1>NEW ENTRY</h1>
                </div>
            </div>

            <div class="bottom-data">
                <div class="orders">
                    <div class="header">
                        <i class='bx bx-shield-plus' ></i>
                        <h3>Enter Account Details</h3>
                    </div>
                    <h3></h3>
                    <div class="details">
                        <form action="#" method="POST">
                            <div class="input-box">
                                <label>Username (or Email)</label>
                                <input type="text" name="username_email" required>
                            </div>
                            <div class="input-box">
                                <label>Account Name</label>
                                <input type="text" name="account_name" required>
                            </div>
                            <div class="input-box">
                                <label>Password</label>
                                <input type="password" name="password" required>
                            </div>
                            <br>
                            <br>
                            <button type="submit" class="btn">Add Account</button>
                        </form>
                    </div>
                </div>
            </div>
        </main>
    </div>
    #<script src="new_entry_script.js"></script>
</body>

</html>

        """
    elif request.method == 'POST':
        # Extract form data and process it
        data = request.form
        username_email = data.get('username_email')
        account_name = data.get('account_name')
        password = data.get('password')
        
        # Save password to database
        with app.app_context():
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO passwords (account_name, username_email, unhashed_password) VALUES (%s, %s, %s)',
                           (account_name, username_email, password))
            mysql.connection.commit()
            cursor.close()
        return redirect('/dashboard')

#------------------------------------------------------------------------------------
# Endpoint for generating a random password suggestion
@app.route('/password_generator', methods=['GET'])
def password_generator():
    if request.method == 'GET':
        return """
        <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
    <link rel="stylesheet" href="/static/password_generator_style.css">
    <title>Responsive Dashboard Design #2 | AsmrProg</title>
</head>

<body>

    <!-- Sidebar -->
    <div class="sidebar">
        <a href="#" class="logo">
            <i class='bx bx-code-alt'></i>
            <div class="logo-name"><span>PS</span>Vault</div>
        </a>
        <ul class="side-menu">
            <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
            <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
            <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
            <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
            <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
            <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
            <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
        </ul>
        <ul class="side-menu">
            <li>
                <a href="#" class="logout">
                    <i class='bx bx-log-out-circle'></i>
                    Logout
                </a>
            </li>
        </ul>
    </div>
    <!-- End of Sidebar -->

    <!-- Main Content -->
    <div class="content">
        <!-- Navbar -->
        <nav>
            <i class='bx bx-menu'></i>
            <form action="#">
                <div class="form-input">
                    <input type="search" placeholder="Search...">
                    <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                </div>
            </form>
            <!--<input type="checkbox" id="theme-toggle" hidden>
            <label for="theme-toggle" class="theme-toggle"></label>
            <a href="#" class="notif">
                <i class='bx bx-bell'></i>
                <span class="count">12</span>
            </a> -->
            <a href="#" class="profile">
                <img src="images/profile-1.jpg">
            </a>
        </nav>

        <!-- End of Navbar -->

        <main>
            <div class="header">
                <div class="left">
                    <h1>Password Generator</h1>
                    <!-- <ul class="breadcrumb">
                        <li><a href="#">
                                Analytics
                            </a></li>
                        <li><a href="#" class="active">Shop</a></li>
                    </ul> -->
                </div>
                <!-- <a href="#" class="report">
                    <i class='bx bx-cloud-download'></i>
                    <span>Download CSV</span>
                </a> -->
            </div>

            <!-- Insights -->
            <!-- <ul class="insights">
                <li>
                    <i class='bx bx-show-alt'></i>
                    <img src="/static/images/Digital Vault.jpg">
                    <span class="info">
                        <h3>
                            3,944
                        </h3>
                        <p>Visit Vault</p>
                    </span>
                </li>
                <li>
                    <i class='bx bx-calendar-check'></i>
                    <img src="/static/images/vault 1_gemini_Generated_Image.jpeg">
                    <span class="info">
                        <h3>
                            1,074
                        </h3>
                        <p>Paid Order</p>
                    </span>
                </li>
                <li>
                    <i class='bx bx-line-chart'></i>
                    <img src="/static/images/key images.webp">
                    <span class="info">
                        <h3>
                            14,721
                        </h3>
                        <p>New Key</p>
                    </span>
                </li>
                <li>
                    <i class='bx bx-dollar-circle'></i>
                    <img src="/static/images/vault_Gemini_Generated_Image.jpeg">
                    <span class="info">
                        <h3>
                            $6,742
                        </h3>
                        <p>New Entry</p>
                    </span>
                </li>
            </ul> -->
            <!-- End of Insights -->

            <div class="bottom-data">
                <!-- <div class="orders"> 
                    <div class="header">
                        <a href="#">
                            <h3>History</h3>
                        </a>
                         <i class='bx bx-filter'></i> 
                        <i class='bx bx-search'></i>
                    </div>
                    <table>
                        <thead>
                            <tr>
                                <th>User</th>
                                <th>Order Date</th>
                                <th>Changes Done</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    
                                    <p>Siddhi Raney</p>
                                </td>
                                <td>10-05-2023</td>
                                <td><span class="status completed">UPDATED</span></td>
                            </tr>
                            <tr>
                                <td>
                                    
                                    <p>User 2</p>
                                </td>
                                <td>11-05-2023</td>
                                <td><span class="status pending">UPDATED</span></td>
                            </tr>
                            <tr>
                                <td>
                                    
                                    <p>Tina Naik</p>
                                </td>
                                <td>15-08-2023</td>
                                <td><span class="status process">UPDATED</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div> -->

                <!-- Reminders -->
                <div class="reminders">
                    <div class="header">
                        <i class='bx bx-dialpad'></i>
                        <h3>Generate New Password</h3>
                        <i class='bx bx-filter'></i>
                        <!-- <i class='bx bx-plus'></i> -->
                    </div>
                    <!-- <ul class="task-list">
                        <li class="completed">
                            <div class="task-title">
                                <i class='bx bx-check-circle'></i>
                                <p class="font-color">It's been 6 months since password change</p>
                            </div>
                            <i class='bx bx-dots-vertical-rounded'></i>
                        </li>
                        <li class="completed">
                            <div class="task-title">
                                <i class='bx bx-check-circle'></i>
                                <p class="font-color">Check your password strength</p>
                            </div>
                            <i class='bx bx-dots-vertical-rounded'></i>
                        </li>
                        <li class="not-completed">
                            <div class="task-title">
                                <i class='bx bx-x-circle'></i>
                                <p class="font-color">ALERT!! 11Password Compromised</p>
                            </div>
                            <i class='bx bx-dots-vertical-rounded'></i>
                        </li>
                    </ul> -->
                    <div class="container">
                        <h1>Password Generator</h1>
                        <br>
                        <form>
                            <div class="form-group">
                                <label>
                                    <input type="checkbox" id="uppercase">Uppercase
                                    <input type="checkbox" id="lowercase">Lowercase
                                    <input type="checkbox" id="numbers">Numbers
                                </label>
                                <br><br>
                                <button type="button" id="generate-btn">Generate Password</button>
                                <br><br>
                                <label for="password">Your Password:</label>
                                <input type="text" id="password" name="password" readonly>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- End of Reminders-->

            </div>

        </main>

    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function () {
            // Function to generate random password
            function generatePassword() {
                // Define characters for different character sets
                const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
                const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
                const numberChars = '0123456789';

                // Function to get a random character from a string
                function getRandomChar(characters) {
                    return characters.charAt(Math.floor(Math.random() * characters.length));
                }

                // Initialize password
                let password = '';

                // Check which character sets are selected
                const uppercaseChecked = document.getElementById('uppercase').checked;
                const lowercaseChecked = document.getElementById('lowercase').checked;
                const numbersChecked = document.getElementById('numbers').checked;

                // Generate password based on selected character sets
                while (password.length < 12) { // Adjust the length as needed
                    if (uppercaseChecked) {
                        password += getRandomChar(uppercaseChars);
                    }
                    if (lowercaseChecked) {
                        password += getRandomChar(lowercaseChars);
                    }
                    if (numbersChecked) {
                        password += getRandomChar(numberChars);
                    }
                }

                // Shuffle the characters in the password
                password = password.split('').sort(() => Math.random() - 0.5).join('');

                // Update password input field
                document.getElementById('password').value = password;
            }

            // Add event listener to the Generate Password button
            document.getElementById('generate-btn').addEventListener('click', generatePassword);
        });
    </script>
</body>

</html>

        """
#-----------------------------------------------------------------------------------------------------------------------

@app.route('/hints', methods=['GET', 'POST'])
def hints():
    
    if request.method == 'GET':
        # Serve HTML form for entering hints
        return """
        <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/hints_style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
    <title>Enter Hint Information</title>
</head>

<body>

    <!-- Sidebar -->
    <div class="sidebar">
        <a href="#" class="logo">
            <i class='bx bx-code-alt'></i>
            <div class="logo-name"><span>PS</span>Vault</div>
        </a>
        <ul class="side-menu">
            <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
            <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
            <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
            <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
            <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
            <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
            <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
        <ul class="side-menu">
            <li>
                <a href="#" class="logout">
                    <i class='bx bx-log-out-circle'></i>
                    Logout
                </a>
            </li>
        </ul>
    </div>
    <!-- End of Sidebar -->

    <!-- Main Content -->
    <div class="content">
        <!-- Navbar -->
        <nav>
            <i class='bx bx-menu'></i>
            <form action="#" method="POST">
                <div class="form-input">
                    <input type="search" placeholder="Search...">
                    <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                </div>
            </form>
            <a href="#" class="profile">
               
            </a>
        </nav>

        <!-- End of Navbar -->

        <main>
            <div class="header">
                <div class="left">
                    <h1>Enter Hint Information</h1>
                </div>
            </div>

            <div class="bottom-data">
                <div class="orders">
                    <div class="header">
                        <i class='bx bx-shield-plus' ></i>
                        <h3>Enter Password Hint </h3>
                    </div>
                    <h3></h3>
                    <div class="details">
                        <form action="#" method="POST">
                            <div class="input-box">
                                <label>Account Name</label>
                                <input type="text" name="username" required>
                            </div>
                            <div class="input-box">
                                <label>Hint Question</label>
                                <input type="text" name="hint_question" required>
                            </div>
                            <div class="input-box">
                                <label>Hint Answer</label>
                                <input type="password" name="hint_answer" required>
                            </div>
                            <br>
                            <br>
                            <button type="submit" class="btn">Submit</button>
                        </form>
                    </div>
                </div>
            </div>
        </main>
    </div>
    #<script src="hints_script.js"></script>
</body>

</html>
        """
    elif request.method == 'POST':
        # Extract form data and process it
        data = request.form
        username = data.get('username')
        hint_question = data.get('hint_question')
        hint_answer = data.get('hint_answer')

        # Save hint to database
        with app.app_context():
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO hints (account_name, hint_question, hint_answer) VALUES (%s, %s, %s)',
                           (username, hint_question, hint_answer))
            mysql.connection.commit()
            cursor.close()

        # Redirect to dashboard after saving the hint
        return redirect('/dashboard')

#----------------------------------------------------------------------------------------------------------------

# Endpoint for checking password strength
@app.route('/strength_meter', methods=['GET'])
def strength_meter():
    if request.method == 'GET':
        return """
        <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
    <link rel="stylesheet" href="/static/strength_meter_style.css">
    <title>Responsive Dashboard Design #2 | AsmrProg</title>
</head>

<body>

    <!-- Sidebar -->
    <div class="sidebar">
        <a href="#" class="logo">
            <i class='bx bx-code-alt'></i>
            <div class="logo-name"><span>PS</span>Vault</div>
        </a>
        <ul class="side-menu">
            <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
            <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
            <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
            <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
            <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
            <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
            <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
        </ul>
        <ul class="side-menu">
            <li>
                <a href="#" class="logout">
                    <i class='bx bx-log-out-circle'></i>
                    Logout
                </a>
            </li>
        </ul>
    </div>
    <!-- End of Sidebar -->

    <!-- Main Content -->
    <div class="content">
        <!-- Navbar -->
        <nav>
            <i class='bx bx-menu'></i>
            <form action="#">
                <div class="form-input">
                    <input type="search" placeholder="Search...">
                    <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                </div>
            </form>
            <a href="#" class="profile">
                
            </a>
        </nav>

        <!-- End of Navbar -->

        <main>
            <div class="header">
                <div class="left">
                    <h1>STRENGTH CHECK</h1>
                </div>
            </div>

            <div class="bottom-data">
                <div class="orders">
                    <div class="header">
                        <i class='bx bx-shield-plus' ></i>
                        <h3>Password Strength Meter</h3>
                    </div>
                    
                    <div class="container">
                        <!-- <h3>Password Strength Meter</h3>
                        <br><br>
                        <input type="password" id="password" placeholder="Enter your password">
                        <br>
                        <br>
                        <div class="pw-display-toggle-btn">
                            <i class="fa fa-eye"></i>
                            <i class="fa fa-eye-slash"></i>
                          </div>
                          <div class="pw-strength">
                            <span>Weak</span>
                            <span></span>
                          </div>
                        <br> -->
                        <div class="pw-meter">
                            <div class="form-element">
                              <label for="password">Password</label>
                              <input type="password" id="password">
                              <div class="pw-display-toggle-btn">
                                <i class="fa fa-eye"></i>
                                <i class="fa fa-eye-slash"></i>
                              </div>
                              <br>
                              <br>
                              <div class="pw-strength">
                                <span>Weak</span>
                                <span></span>
                              </div>
                            </div>
                          </div>
                    </div>
                    

                    <!-- <div class="pw-meter">
                        <div class="container">
                            <h3>Password Strength Meter</h3>
                            <br><br>
                            <input type="password" id="passwordInput" placeholder="Enter your password">
                            <br>
                            <br>
                            <div id="strengthText"></div>
                            <br>
                        </div>
                    </div> -->
                        
                </div>
            </div>
        </main>
    </div>
    <script src="/static/strength_meter_script.js"></script>
</body>

</html>
        """
#-----------------------------------------------------------------------------------------------------
#update which re-directs to update password or update vault password

@app.route('/update', methods=['GET'])
def update():
    if request.method == 'GET':
        return """
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
            <link rel="stylesheet" href="/static/update_style.css">
            <title>Responsive Dashboard Design #2 | AsmrProg</title>
        </head>

        <body>

            <!-- Sidebar -->
            <div class="sidebar">
                <a href="#" class="logo">
                    <i class='bx bx-code-alt'></i>
                    <div class="logo-name"><span>PS</span>Vault</div>
                </a>
                <ul class="side-menu">
                    <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
                    <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
                    <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
                    <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
                    <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
                    <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
                    <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
                </ul>
                <ul class="side-menu">
                    <li>
                        <a href="#" class="logout">
                            <i class='bx bx-log-out-circle'></i>
                            Logout
                        </a>
                    </li>
                </ul>
            </div>
            <!-- End of Sidebar -->

            <!-- Main Content -->
            <div class="content">
                <!-- Navbar -->
                <nav>
                    <i class='bx bx-menu'></i>
                    <form action="#">
                        <div class="form-input">
                            <input type="search" placeholder="Search...">
                            <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                        </div>
                    </form>
                    <a href="#" class="profile">
                        
                    </a>
                </nav>

                <!-- End of Navbar -->

                <main>
                    <div class="header">
                        <div class="left">
                            <h1>UPDATE ACCOUNT</h1>
                        </div>
                    </div>

                    <div class="bottom-data">
                        <div class="orders">
                            <div class="container">
                                <a href="/update_account">Update Account Password</a>
                                <br>
                                <br>
                                <br>
                                <a href="/update_vault">Update Vault Password</a>
                                <br>
                                <p id="strengthText"></p>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
            <!-- End of Main Content -->

            <script src="update_script.js"></script>
        </body>

        </html>
        """

#-----------------------------------------------------------------------------------------------------------

@app.route('/update_account', methods=['GET', 'POST'])
def update_account():
    if request.method == 'POST':
        account_name = request.form['account_name']
        question_hint = request.form['question_hint']
        hint_answer = request.form['hint_answer']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        if new_password != confirm_password:
            return "New password and confirm password do not match. Please try again."
        
        with app.app_context():
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM hints WHERE account_name = %s AND hint_question = %s AND hint_answer = %s", (account_name, question_hint, hint_answer))
            hint_data = cursor.fetchone()
            
            if hint_data:
                # Update password if hint question and hint answer match
                cursor.execute("UPDATE passwords SET unhashed_password = %s WHERE account_name = %s", (new_password, account_name))
                mysql.connection.commit()
                cursor.close()
                
               # return redirect('/login') 
            else:
                return "Hint question and hint answer do not match for the provided account. Please try again."
    
    # HTML code for the update account form
    return """
   <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/update_vault_style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
    <title>Update Vault</title>
</head>

<body>

    <!-- Sidebar -->
    <div class="sidebar">
        <a href="#" class="logo">
            <i class='bx bx-code-alt'></i>
            <div class="logo-name"><span>PS</span>Vault</div>
        </a>
        <ul class="side-menu">
            <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
            <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
            <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
            <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
            <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
            <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
            <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
        </ul>
        <ul class="side-menu">
            <li>
                <a href="#" class="logout">
                    <i class='bx bx-log-out-circle'></i>
                    Logout
                </a>
            </li>
        </ul>
    </div>
    <!-- End of Sidebar -->

    <!-- Main Content -->
    <div class="content">
        <!-- Navbar -->
        <nav>
            <i class='bx bx-menu'></i>
            <form action="#">
                <div class="form-input">
                    <input type="search" placeholder="Search...">
                    <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                </div>
            </form>
            <a href="#" class="profile">
                
            </a>
        </nav>

        <!-- End of Navbar -->

        <main>
            <div class="header">
                <div class="left">
                    <h1>UPDATE ACCOUNT</h1>
                </div>
            </div>

            <div class="bottom-data">
                <div class="orders">
                    <h3></h3>
                    <div class="details">
                        <form method="post" action="/update_account">
                            <div class="input-box">
                                <label>Account Name</label>
                                <input type="text" name="account_name" required>
                            </div>
                            <div class="input-box">
                                <label>Question Hint</label>
                                <input type="text" name="question_hint" required>
                            </div>
                            <div class="input-box">
                                <label>Hint Answer</label>
                                <input type="text" name="hint_answer" required>
                            </div>
                            <div class="input-box">
                                <label>New Password</label>
                                <input type="password" name="new_password" required>
                            </div>
                            <div class="input-box">
                                <label>Confirm Password</label>
                                <input type="password" name="confirm_password" required>
                            </div>
                            <br>
                            <button type="submit" class="btn">Update</button>
                        </form>
                    </div>
                </div>
            </div>
        </main>
    </div>
</body>

</html>
        """

    
#-----------------------------------------------------------------------------------------------------------
@app.route('/update_vault', methods=['GET', 'POST'])
def update_vault():
    if request.method == 'POST':
        username = request.form['username']
        emergency_contact = request.form['emergency_contact']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        if new_password != confirm_password:
            return "New password and confirm password do not match. Please try again."
        
        with app.app_context():
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND emergency_contact = %s", (username, emergency_contact))
            user_data = cursor.fetchone()
            
            if user_data:
                # Update password if username and emergency contact match
                cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
                mysql.connection.commit()
                cursor.close()
                
                return redirect('/login') 
            else:
                return "Username and emergency contact do not match. Please try again."
    
    # HTML code for the update vault form
    return """
   <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/update_vault_style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
    <title>Responsive Dashboard Design #2 | AsmrProg</title>
</head>

<body>

    <!-- Sidebar -->
    <div class="sidebar">
        <a href="#" class="logo">
            <i class='bx bx-code-alt'></i>
            <div class="logo-name"><span>PS</span>Vault</div>
        </a>
        <ul class="side-menu">
            <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
            <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
            <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
            <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
            <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
            <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
            <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
        </ul>
        <ul class="side-menu">
            <li>
                <a href="#" class="logout">
                    <i class='bx bx-log-out-circle'></i>
                    Logout
                </a>
            </li>
        </ul>
    </div>
    <!-- End of Sidebar -->

    <!-- Main Content -->
    <div class="content">
        <!-- Navbar -->
        <nav>
            <i class='bx bx-menu'></i>
            <form action="#">
                <div class="form-input">
                    <input type="search" placeholder="Search...">
                    <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                </div>
            </form>
            <a href="#" class="profile">
                
            </a>
        </nav>

        <!-- End of Navbar -->

        <main>
            <div class="header">
                <div class="left">
                    <h1>UPDATE VAULT</h1>
                </div>
            </div>

            <div class="bottom-data">
                <div class="orders">
                    <!-- <div class="header">
                        <i class='bx bx-shield-plus' ></i>
                        <h3>Enter Vault Details</h3>
                    </div> -->
                    <h3></h3>
                    <div class="details">
                        <form method="post" action="/update_vault">
                            <div class="input-box">
                                <label>Username</label>
                                <input type="text" name="username" required>
                                <!-- <i class='bx bx-user'></i> -->
                            </div>
                            <div class="input-box">
                                <label>Emergency Contact</label>
                                <input type="text" name="emergency_contact" required>
                                <!-- <i class='bx bx-link-alt'></i> -->
                            </div>
                            <div class="input-box">
                                <label>New Password</label>
                                <input type="password" name="new_password" required>
                                <!-- <i class='bx bxs-lock-alt'></i> -->
                            </div>
                            <div class="input-box">
                                <label>Confirm Password</label>
                                <input type="password" name="confirm_password" required>
                                <!-- <i class='bx bxs-lock-alt'></i> -->
                            </div>
                            <br>
                            <br>
                            <button type="submit" class="btn">Update</button>
                        </form>
                    </div>
                </div>
            </div>
        </main>
    </div>
    <script src="update_vault_script.js"></script>
</body>

</html>


        """

#---------------------------------------------------------------------------------------------------------------
@app.route('/history', methods=['GET'])
def history():
    # Fetch login history from the database
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT account_name FROM passwords')
        history_data = cursor.fetchall()
        cursor.close()

        # Start building HTML content
        html_template = """
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/static/history_style.css">
            <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
            <title>Responsive Dashboard Design #2 | AsmrProg</title>
        </head>

        <body>

            <!-- Sidebar -->
            <div class="sidebar">
                <a href="#" class="logo">
                    <i class='bx bx-code-alt'></i>
                    <div class="logo-name"><span>PS</span>Vault</div>
                </a>
                <ul class="side-menu">
                    <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
                    <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
                    <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
                    <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
                    <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
                    <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
                    <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
                </ul>
                <ul class="side-menu">
                    <li>
                        <a href="#" class="logout">
                            <i class='bx bx-log-out-circle'></i>
                            Logout
                        </a>
                    </li>
                </ul>
            </div>
            <!-- End of Sidebar -->

            <!-- Main Content -->
            <div class="content">
                <!-- Navbar -->
                <nav>
                    <i class='bx bx-menu'></i>
                    <form action="#">
                        <div class="form-input">
                            <input type="search" placeholder="Search...">
                            <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                        </div>
                    </form>
                    <!--<input type="checkbox" id="theme-toggle" hidden>
                    <label for="theme-toggle" class="theme-toggle"></label>
                    <a href="#" class="notif">
                        <i class='bx bx-bell'></i>
                        <span class="count">12</span>
                    </a> -->
                    <a href="#" class="profile">
                       
                    </a>
                </nav>

                <!-- End of Navbar -->

                <main>
                    <div class="header">
                        <div class="left">
                            <h1>HISTORY</h1>
                        </div>
                    </div>

                    <div class="bottom-data">
                        <div class="orders">
                            <div class="header">
                                <i class='bx bx-receipt'></i>
                                <h3>Your Activity</h3>
                            </div>
                            <table>
                                <thead>
                                    <tr>
                                        <th>Account Name</th>
                                        <th>Status</th>
                                    </tr>
                                </thead>
                                <tbody>
        """

        # Populate table rows with data
        for data in history_data:
            html_template += """
                                    <tr>
                                        <td>
                                            <i class='bx bx-envelope'></i>
                                            <p>{}</p>
                                        </td>
                                        <td>UPDATED</td>
                                    </tr>
            """.format(data[0])

        # Close HTML content
        html_template += """
                                </tbody>
                            </table>
                        </div>
                    </div>
                </main>

            </div>

            <script src="my_vault_script.js"></script>
        </body>

        </html>
        """

    return html_template


   
#------------------------------------------------------------------------------------------------------
@app.route('/my_vault', methods=['GET'])
def my_vault():
    try:
        with app.app_context():
            cursor = mysql.connection.cursor()
            # Adjust the query to fetch all rows from the passwords and hints tables
            query = '''
                SELECT p.account_name, p.username_email, p.unhashed_password, h.hint_question, h.hint_answer 
                FROM passwords p 
                LEFT JOIN hints h ON p.account_name = h.account_name
            '''

            cursor.execute(query)
            vault_data = cursor.fetchall()
            cursor.close()

        # Construct vault_entries list to hold all values from the database
        vault_entries = [{'account_name': row[0], 'username_email': row[1], 'unhashed_password': row[2], 'hint_question': row[3], 'hint_answer': row[4]} for row in vault_data]

    except Exception as e:
        print(f"Error fetching data: {e}")
        vault_entries = []

    # HTML template for displaying the vault data
    html_template = """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/my_vault_style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
    <title>Responsive Dashboard Design #2 | AsmrProg</title>
</head>

<body>

    <!-- Sidebar -->
    <div class="sidebar">
        <a href="#" class="logo">
            <i class='bx bx-code-alt'></i>
            <div class="logo-name"><span>PS</span>Vault</div>
        </a>
        <ul class="side-menu">
            <li><a href="/dashboard"><i class='bx bxs-dashboard'></i>Dashboard</a></li>
            <li><a href="/emergency_contacts"><i class='bx bx-store-alt'></i>Emergency Contacts</a></li>
            <li><a href="/hints"><i class='bx bx-store-alt'></i>Hints</a></li>
            <li><a href="/password_generator"><i class='bx bx-cog'></i>Password Generator</a></li>
            <li><a href="/strength_meter"><i class='bx bx-analyse'></i>Strength Check</a></li>
            <li><a href="/history"><i class='bx bx-group'></i>History</a></li>
            <li><a href="/update"><i class='bx bx-cog'></i>Update</a></li>
        </ul>
        <ul class="side-menu">
            <li>
                <a href="/logout" class="logout">
                    <i class='bx bx-log-out-circle'></i>
                    Logout
                </a>
            </li>
        </ul>
    </div>
    <!-- End of Sidebar -->

    <!-- Main Content -->
    <div class="content">
        <!-- Navbar -->
        <nav>
            <i class='bx bx-menu'></i>
            <form action="#">
                <div class="form-input">
                    <input type="search" placeholder="Search...">
                    <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                </div>
            </form>
            <a href="#" class="profile">
               
            </a>
        </nav>
        <!-- End of Navbar -->

        <main>
            <div class="header">
                <div class="left">
                    <h1>MY VAULT</h1>
                </div>
            </div>

            <div class="bottom-data">
                <div class="orders">
                    <div class="header">
                        <i class='bx bx-receipt'></i>
                        <h3>ENTER DETAILS</h3>
                        <i class='bx bx-plus'></i>
                        <i class='bx bx-search'></i>
                    </div>
                    <table>
                        <thead>
                            <tr>
                                <th>Account Name</th>
                                <th>Username/Email</th>
                                <th>Password</th>
                                <th>Hint Question</th>
                                <th>Hint Answer</th>
                            </tr>
                        </thead>
                        <tbody>
    """

    for entry in vault_entries:
        html_template += f"""
                            <tr>
                                <td>{entry['account_name']}</td>
                                <td>{entry['username_email']}</td>
                                <td>{entry['unhashed_password']}</td>
                                <td>{entry['hint_question']}</td>
                                <td>{entry['hint_answer']}</td>
                            </tr>
        """

    html_template += """
                        </tbody>
                    </table>
                    <br>
                    <a href="/update_account" class="btn">Update</a>
                </div>
            </div>
        </main>
    </div>

    <script src="/static/my_vault_script.js"></script>
</body>
</html>
    """
    return (html_template)
#--------------------------------------------------------------------------------------------------------
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form['username']
        emergency_contact = request.form['emergency_contact']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        if new_password != confirm_password:
            return "New password and confirm password do not match. Please try again."
        
        with app.app_context():
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND emergency_contact = %s", (username, emergency_contact))
            user_data = cursor.fetchone()
            
            if user_data:
                # Update password if username and emergency contact match
                cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
                mysql.connection.commit()
                cursor.close()
                
                return redirect('/login') 
            else:
                return "Username and emergency contact do not match. Please try again."
    
    
    # HTML code for the forgot password form
    return """
   <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/update_vault_style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
    <title>Forgot Password | AsmrProg</title>
</head>

<body>

    <!-- Main Content -->
    <div class="content">
        <!-- Navbar -->
        <nav>
            <i class='bx bx-menu'></i>
            <form action="#">
                <div class="form-input">
                    <input type="search" placeholder="Search...">
                    <button class="search-btn" type="submit"><i class='bx bx-search'></i></button>
                </div>
            </form>
            <a href="#" class="profile">
                
            </a>
        </nav>
        <!-- End of Navbar -->

        <main>
            <div class="header">
                <div class="left">
                    <h1>FORGOT PASSWORD</h1>
                </div>
            </div>

            <div class="bottom-data">
                <div class="orders">
                    <h3></h3>
                    <div class="details">
                        <form method="post" action="/forgot_password">
                            <div class="input-box">
                                <label>Username</label>
                                <input type="text" name="username" required>
                            </div>
                            <div class="input-box">
                                <label>Emergency Contact</label>
                                <input type="text" name="emergency_contact" required>
                            </div>
                            <div class="input-box">
                                <label>New Password</label>
                                <input type="password" name="new_password" required>
                            </div>
                            <div class="input-box">
                                <label>Confirm Password</label>
                                <input type="password" name="confirm_password" required>
                            </div>
                            <br>
                            <br>
                            <button type="submit" class="btn">LOGIN</button>
                        </form>
                    </div>
                </div>
            </div>
        </main>
    </div>
    <script src="update_vault_script.js"></script>
</body>

</html>
    """


#----------------------------------------------------------------------------------------------------------------
# Endpoint for user logout
@app.route('/logout', methods=['GET'])
def logout():
    return redirect('/sign_up')
#-------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)


