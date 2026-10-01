from flask import Flask, render_template_string

app = Flask(__name__)


# ============================================================
# HTML + CSS
# ============================================================

HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Your Name | Resume</title>

    <style>

        /* =====================================================
           GENERAL
        ===================================================== */

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f4f6f9;
        }

        a {
            text-decoration: none;
            color: #2563eb;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: auto;
        }


        /* =====================================================
           HEADER
        ===================================================== */

        .header {
            background: linear-gradient(
                135deg,
                #1e3a8a,
                #2563eb
            );

            color: white;
            padding: 70px 0;
        }

        .profile {
            display: flex;
            align-items: center;
            gap: 35px;
        }

        .profile-image {
            width: 150px;
            height: 150px;

            border-radius: 50%;

            background: white;
            color: #2563eb;

            display: flex;
            justify-content: center;
            align-items: center;

            font-size: 45px;
            font-weight: bold;

            border: 6px solid rgba(255,255,255,0.3);
        }

        .profile-info {
            flex: 1;
        }

        .profile-info h1 {
            font-size: 48px;
            margin-bottom: 5px;
        }

        .profile-info h2 {
            font-size: 22px;
            font-weight: normal;
            color: #dbeafe;
            margin-bottom: 15px;
        }

        .profile-info p {
            max-width: 700px;
            color: #e5e7eb;
            margin-bottom: 20px;
        }

        .contact-info {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            font-size: 14px;
        }


        /* =====================================================
           NAVIGATION
        ===================================================== */

        .navbar {
            background: white;

            position: sticky;
            top: 0;

            z-index: 100;

            box-shadow:
                0 2px 8px rgba(0,0,0,0.1);
        }

        .nav-container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
        }

        .nav-container a {
            color: #333;

            padding: 16px 20px;

            font-weight: 600;

            transition: 0.3s;
        }

        .nav-container a:hover {
            color: white;
            background: #2563eb;
        }


        /* =====================================================
           MAIN
        ===================================================== */

        .main-content {
            padding-top: 30px;
            padding-bottom: 30px;
        }

        .section {
            background: white;

            padding: 35px;

            margin-bottom: 30px;

            border-radius: 10px;

            box-shadow:
                0 3px 15px rgba(0,0,0,0.06);
        }

        .section-title {
            font-size: 28px;

            color: #1e3a8a;

            margin-bottom: 25px;

            padding-bottom: 10px;

            border-bottom: 3px solid #2563eb;
        }

        .section p {
            margin-bottom: 15px;
            color: #555;
        }


        /* =====================================================
           SKILLS
        ===================================================== */

        .skills-container {
            display: grid;

            grid-template-columns:
                repeat(2, 1fr);

            gap: 25px;
        }

        .skill h3 {
            margin-bottom: 8px;
            color: #333;
        }

        .progress {
            height: 10px;

            background: #e5e7eb;

            border-radius: 10px;

            overflow: hidden;
        }

        .progress-bar {
            height: 100%;

            background: #2563eb;

            border-radius: 10px;
        }

        .python {
            width: 90%;
        }

        .flask {
            width: 85%;
        }

        .html {
            width: 95%;
        }

        .css {
            width: 90%;
        }

        .javascript {
            width: 75%;
        }

        .sql {
            width: 80%;
        }


        /* =====================================================
           EXPERIENCE
        ===================================================== */

        .timeline {
            position: relative;

            margin-left: 15px;

            padding-left: 30px;

            border-left: 3px solid #dbeafe;
        }

        .timeline-item {
            position: relative;
            margin-bottom: 40px;
        }

        .timeline-item:last-child {
            margin-bottom: 0;
        }

        .timeline-dot {
            position: absolute;

            width: 15px;
            height: 15px;

            border-radius: 50%;

            background: #2563eb;

            left: -39px;
            top: 5px;

            border: 3px solid white;

            box-shadow:
                0 0 0 2px #2563eb;
        }

        .date {
            display: inline-block;

            color: #2563eb;

            font-size: 14px;

            font-weight: bold;

            margin-bottom: 5px;
        }

        .timeline-content h3 {
            font-size: 22px;
            color: #1f2937;
        }

        .timeline-content h4 {
            color: #666;
            margin-bottom: 10px;
        }

        .timeline-content ul {
            margin-left: 20px;
            color: #555;
        }

        .timeline-content li {
            margin-bottom: 5px;
        }


        /* =====================================================
           EDUCATION
        ===================================================== */

        .education-card {
            display: flex;

            gap: 20px;

            padding: 25px;

            background: #f8fafc;

            border-left: 5px solid #2563eb;

            margin-bottom: 20px;

            border-radius: 5px;
        }

        .education-card:last-child {
            margin-bottom: 0;
        }

        .education-icon {
            font-size: 35px;
        }

        .education-card h3 {
            color: #1f2937;
            margin-bottom: 5px;
        }

        .education-card h4 {
            color: #2563eb;
            margin-bottom: 5px;
        }

        .education-card span {
            font-size: 14px;
            color: #777;
        }

        .education-card p {
            margin-top: 10px;
        }


        /* =====================================================
           PROJECTS
        ===================================================== */

        .projects-grid {
            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 20px;
        }

        .project-card {
            padding: 25px;

            background: #f8fafc;

            border-radius: 8px;

            border: 1px solid #e5e7eb;

            transition: 0.3s;
        }

        .project-card:hover {
            transform: translateY(-5px);

            box-shadow:
                0 8px 20px rgba(0,0,0,0.1);

            border-color: #2563eb;
        }

        .project-icon {
            font-size: 40px;
            margin-bottom: 15px;
        }

        .project-card h3 {
            color: #1f2937;
            margin-bottom: 10px;
        }

        .project-card p {
            font-size: 14px;
        }

        .project-tags {
            display: flex;

            flex-wrap: wrap;

            gap: 7px;

            margin-top: 15px;
        }

        .project-tags span {
            background: #dbeafe;

            color: #1e40af;

            padding: 5px 10px;

            border-radius: 15px;

            font-size: 12px;
        }


        /* =====================================================
           CONTACT
        ===================================================== */

        .contact-grid {
            display: grid;

            grid-template-columns:
                repeat(4, 1fr);

            gap: 15px;
        }

        .contact-card {
            text-align: center;

            padding: 25px 15px;

            background: #f8fafc;

            border-radius: 8px;

            border: 1px solid #e5e7eb;
        }

        .contact-icon {
            font-size: 30px;
            margin-bottom: 10px;
        }

        .contact-card h3 {
            margin-bottom: 5px;
            color: #1f2937;
        }

        .contact-card p,
        .contact-card a {
            font-size: 13px;
            word-break: break-word;
        }


        /* =====================================================
           FOOTER
        ===================================================== */

        footer {
            background: #111827;

            color: white;

            text-align: center;

            padding: 30px 0;
        }

        footer p {
            margin-bottom: 5px;

            color: #d1d5db;

            font-size: 14px;
        }


        /* =====================================================
           RESPONSIVE
        ===================================================== */

        @media (max-width: 900px) {

            .projects-grid {
                grid-template-columns:
                    repeat(2, 1fr);
            }

            .contact-grid {
                grid-template-columns:
                    repeat(2, 1fr);
            }
        }


        @media (max-width: 700px) {

            .profile {
                flex-direction: column;
                text-align: center;
            }

            .profile-info h1 {
                font-size: 36px;
            }

            .profile-info h2 {
                font-size: 18px;
            }

            .contact-info {
                justify-content: center;
            }

            .skills-container {
                grid-template-columns: 1fr;
            }

            .projects-grid {
                grid-template-columns: 1fr;
            }

            .contact-grid {
                grid-template-columns: 1fr;
            }

            .nav-container a {
                padding: 10px 12px;
                font-size: 14px;
            }
        }


        @media (max-width: 500px) {

            .section {
                padding: 25px 20px;
            }

            .profile-image {
                width: 120px;
                height: 120px;
                font-size: 35px;
            }

            .profile-info h1 {
                font-size: 30px;
            }

            .timeline {
                margin-left: 5px;
                padding-left: 25px;
            }

            .timeline-dot {
                left: -34px;
            }
        }

    </style>
</head>


<body>


    <!-- =====================================================
         HEADER
    ====================================================== -->

    <header class="header">

        <div class="container">

            <div class="profile">

                <div class="profile-image">
                    YN
                </div>

                <div class="profile-info">

                    <h1>
                        Your Name
                    </h1>

                    <h2>
                        Python Developer & Web Developer
                    </h2>

                    <p>
                        I build clean, responsive and user-friendly
                        web applications using Python and Flask.
                    </p>

                    <div class="contact-info">

                        <span>
                            📧 your.email@gmail.com
                        </span>

                        <span>
                            📱 +91 98765 43210
                        </span>

                        <span>
                            📍 Pune, India
                        </span>

                    </div>

                </div>

            </div>

        </div>

    </header>


    <!-- =====================================================
         NAVIGATION
    ====================================================== -->

    <nav class="navbar">

        <div class="container nav-container">

            <a href="#about">
                About
            </a>

            <a href="#skills">
                Skills
            </a>

            <a href="#experience">
                Experience
            </a>

            <a href="#education">
                Education
            </a>

            <a href="#projects">
                Projects
            </a>

            <a href="#contact">
                Contact
            </a>

        </div>

    </nav>


    <!-- =====================================================
         MAIN
    ====================================================== -->

    <main class="container main-content">


        <!-- ABOUT -->

        <section id="about" class="section">

            <h2 class="section-title">
                About Me
            </h2>

            <p>
                I am a passionate Python developer with an interest
                in web development and software engineering.
                I enjoy creating useful applications and solving
                real-world problems through technology.
            </p>

            <p>
                I have experience working with Python, Flask,
                HTML, CSS, JavaScript and SQL. I am continuously
                learning new technologies and improving my
                development skills.
            </p>

        </section>


        <!-- SKILLS -->

        <section id="skills" class="section">

            <h2 class="section-title">
                Skills
            </h2>

            <div class="skills-container">


                <div class="skill">

                    <h3>
                        Python
                    </h3>

                    <div class="progress">

                        <div class="progress-bar python">
                        </div>

                    </div>

                </div>


                <div class="skill">

                    <h3>
                        Flask
                    </h3>

                    <div class="progress">

                        <div class="progress-bar flask">
                        </div>

                    </div>

                </div>


                <div class="skill">

                    <h3>
                        HTML
                    </h3>

                    <div class="progress">

                        <div class="progress-bar html">
                        </div>

                    </div>

                </div>


                <div class="skill">

                    <h3>
                        CSS
                    </h3>

                    <div class="progress">

                        <div class="progress-bar css">
                        </div>

                    </div>

                </div>


                <div class="skill">

                    <h3>
                        JavaScript
                    </h3>

                    <div class="progress">

                        <div class="progress-bar javascript">
                        </div>

                    </div>

                </div>


                <div class="skill">

                    <h3>
                        SQL
                    </h3>

                    <div class="progress">

                        <div class="progress-bar sql">
                        </div>

                    </div>

                </div>

            </div>

        </section>


        <!-- EXPERIENCE -->

        <section id="experience" class="section">

            <h2 class="section-title">
                Experience
            </h2>

            <div class="timeline">


                <div class="timeline-item">

                    <div class="timeline-dot">
                    </div>

                    <div class="timeline-content">

                        <span class="date">
                            2024 - Present
                        </span>

                        <h3>
                            Python Developer
                        </h3>

                        <h4>
                            ABC Technologies
                        </h4>

                        <p>
                            Developed web applications using
                            Python and Flask. Created APIs,
                            integrated databases and improved
                            application functionality.
                        </p>

                        <ul>

                            <li>
                                Developed Flask web applications.
                            </li>

                            <li>
                                Created REST APIs.
                            </li>

                            <li>
                                Worked with SQL databases.
                            </li>

                            <li>
                                Fixed bugs and improved performance.
                            </li>

                        </ul>

                    </div>

                </div>


                <div class="timeline-item">

                    <div class="timeline-dot">
                    </div>

                    <div class="timeline-content">

                        <span class="date">
                            2023 - 2024
                        </span>

                        <h3>
                            Web Developer Intern
                        </h3>

                        <h4>
                            XYZ Solutions
                        </h4>

                        <p>
                            Worked on frontend and backend
                            web development projects and
                            gained practical experience
                            with Flask.
                        </p>

                        <ul>

                            <li>
                                Created responsive webpages.
                            </li>

                            <li>
                                Worked with Flask.
                            </li>

                            <li>
                                Used HTML and CSS.
                            </li>

                        </ul>

                    </div>

                </div>


            </div>

        </section>


        <!-- EDUCATION -->

        <section id="education" class="section">

            <h2 class="section-title">
                Education
            </h2>


            <div class="education-card">

                <div class="education-icon">
                    🎓
                </div>

                <div>

                    <h3>
                        Bachelor of Computer Science
                    </h3>

                    <h4>
                        ABC University
                    </h4>

                    <span>
                        2020 - 2024
                    </span>

                    <p>
                        Studied programming, databases,
                        web development, software engineering
                        and computer science fundamentals.
                    </p>

                </div>

            </div>


            <div class="education-card">

                <div class="education-icon">
                    📚
                </div>

                <div>

                    <h3>
                        Higher Secondary Education
                    </h3>

                    <h4>
                        ABC Junior College
                    </h4>

                    <span>
                        2018 - 2020
                    </span>

                    <p>
                        Completed higher secondary education
                        with a focus on mathematics and
                        computer science.
                    </p>

                </div>

            </div>

        </section>


        <!-- PROJECTS -->

        <section id="projects" class="section">

            <h2 class="section-title">
                Projects
            </h2>

            <div class="projects-grid">


                <div class="project-card">

                    <div class="project-icon">
                        💼
                    </div>

                    <h3>
                        Resume Website
                    </h3>

                    <p>
                        A personal resume website built
                        using Python Flask, HTML and CSS.
                    </p>

                    <div class="project-tags">

                        <span>
                            Python
                        </span>

                        <span>
                            Flask
                        </span>

                        <span>
                            HTML
                        </span>

                        <span>
                            CSS
                        </span>

                    </div>

                </div>


                <div class="project-card">

                    <div class="project-icon">
                        ✅
                    </div>

                    <h3>
                        Task Management System
                    </h3>

                    <p>
                        A web application that allows users
                        to create, update and delete tasks.
                    </p>

                    <div class="project-tags">

                        <span>
                            Python
                        </span>

                        <span>
                            Flask
                        </span>

                        <span>
                            SQLite
                        </span>

                    </div>

                </div>


                <div class="project-card">

                    <div class="project-icon">
                        👨‍🎓
                    </div>

                    <h3>
                        Student Management System
                    </h3>

                    <p>
                        A CRUD application for managing
                        student information and academic
                        records.
                    </p>

                    <div class="project-tags">

                        <span>
                            Python
                        </span>

                        <span>
                            Flask
                        </span>

                        <span>
                            SQL
                        </span>

                    </div>

                </div>


            </div>

        </section>


        <!-- CONTACT -->

        <section id="contact" class="section">

            <h2 class="section-title">
                Contact Me
            </h2>

            <div class="contact-grid">


                <div class="contact-card">

                    <div class="contact-icon">
                        📧
                    </div>

                    <h3>
                        Email
                    </h3>

                    <a href="mailto:your.email@gmail.com">
                        your.email@gmail.com
                    </a>

                </div>


                <div class="contact-card">

                    <div class="contact-icon">
                        📱
                    </div>

                    <h3>
                        Phone
                    </h3>

                    <p>
                        +91 98765 43210
                    </p>

                </div>


                <div class="contact-card">

                    <div class="contact-icon">
                        📍
                    </div>

                    <h3>
                        Location
                    </h3>

                    <p>
                        Pune, Maharashtra, India
                    </p>

                </div>


                <div class="contact-card">

                    <div class="contact-icon">
                        💻
                    </div>

                    <h3>
                        GitHub
                    </h3>

                    <a href="https://github.com/"
                       target="_blank">
                        github.com/yourusername
                    </a>

                </div>


            </div>

        </section>


    </main>


    <!-- =====================================================
         FOOTER
    ====================================================== -->

    <footer>

        <div class="container">

            <p>
                © 2026 Your Name. All Rights Reserved.
            </p>

            <p>
                Built with Python & Flask
            </p>

        </div>

    </footer>


</body>

</html>
"""


# ============================================================
# ROUTE
# ============================================================

@app.route("/")
def home():
    return render_template_string(HTML)


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
