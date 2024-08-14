<!-- Project Title -->
<h1 align="center">BizCardX: Extracting Business Card Data with OCR</h1>
<p align="center">A Streamlit Application for Extracting and Managing Business Card Information</p>

<!-- Shields.io badges for GitHub stats -->
<p align="center">
    <img src="https://img.shields.io/github/stars/Gowthame123/Bizcardx-extraction-using-OCR-" alt="Stars">
    <img src="https://img.shields.io/github/forks/Gowthame123/Bizcardx-extraction-using-OCR-" alt="Forks">
    <img src="https://img.shields.io/github/issues/Gowthame123/Bizcardx-extraction-using-OCR-" alt="Issues">
    <img src="https://img.shields.io/github/license/Gowthame123/Bizcardx-extraction-using-OCR-" alt="License">
</p>

<!-- Table of Contents -->
<h2>Table of Contents</h2>
<ul>
    <li><a href="#technologies">Technologies</a></li>
    <li><a href="#problem-statement">Problem Statement</a></li>
    <li><a href="#approach">Approach</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#contact">Contact</a></li>
</ul>

<!-- Technologies section -->
<h2 id="technologies">Technologies</h2>
<p>The following technologies were used in this project:</p>
<ul>
    <li>OCR (easyOCR)</li>
    <li>Streamlit GUI</li>
    <li>SQL (SQLite/MySQL)</li>
    <li>Data Extraction</li>
</ul>

<!-- Problem Statement section -->
<h2 id="problem-statement">Problem Statement</h2>
<p>
    The goal of this project is to develop a Streamlit application that allows users to upload an image of a business card and extract relevant information from it using easyOCR. The extracted information should include the company name, cardholder name, designation, mobile number, email address, website URL, area, city, state, and pin code. The extracted information should be displayed in the application's graphical user interface (GUI).
</p>
<p>
    Additionally, the application should allow users to save the extracted information into a database along with the uploaded business card image. The database should store multiple entries, each with its own business card image and extracted information. Users should also be able to read, update, and delete the data through the Streamlit UI.
</p>
<p>
    This project requires skills in image processing, OCR, GUI development, and database management. It also necessitates careful design and planning to ensure the application is scalable, maintainable, and extensible. Good documentation and code organization are also critical for this project.
</p>

<!-- Approach section -->
<h2 id="approach">Approach</h2>
<p>The project approach is divided into the following steps:</p>
<ol>
    <li><strong>Install Required Packages:</strong> Install Python, Streamlit, easyOCR, and a database management system like SQLite or MySQL.</li>
    <li><strong>Design User Interface:</strong> Create a simple and intuitive user interface using Streamlit that guides users through uploading the business card image and extracting its information. Utilize widgets like file uploaders, buttons, and text boxes for interactivity.</li>
    <li><strong>Implement Image Processing and OCR:</strong> Use easyOCR to extract relevant information from the uploaded business card image. Apply image processing techniques like resizing, cropping, and thresholding to enhance image quality before passing it to the OCR engine.</li>
    <li><strong>Display Extracted Information:</strong> Present the extracted information in a clean and organized manner within the Streamlit GUI. Utilize widgets like tables, text boxes, and labels.</li>
    <li><strong>Implement Database Integration:</strong> Use a database management system like SQLite or MySQL to store the extracted information along with the uploaded business card image. Implement CRUD operations (Create, Read, Update, Delete) through the Streamlit UI.</li>
    <li><strong>Test the Application:</strong> Thoroughly test the application to ensure it functions as expected. Run the application locally using the command <code>streamlit run app.py</code>.</li>
    <li><strong>Improve the Application:</strong> Continuously enhance the application by adding new features, optimizing the code, and fixing bugs. Consider adding user authentication and authorization for added security.</li>
</ol>

<!-- Results section -->
<h2 id="results">Results</h2>
<p>
    The final outcome of this project will be a fully functional Streamlit application that allows users to extract, manage, and store information from business cards. The application will feature an intuitive user interface and robust backend integration with a database. Users will have the ability to upload images, extract information, and perform CRUD operations on the stored data.
</p>

<!-- Contact section -->
<h2 id="contact">Contact</h2>
<p>If you want to get in touch, you can find me on:</p>
<p>
    <a href="https://www.linkedin.com/in/gowthamesakki/" target="_blank">
        <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="Gowtham E" height="30" width="40" />
    </a>
</p>

<!-- Footer with acknowledgments -->
<h2>Acknowledgments</h2>
<p>Mention any resources, libraries, or contributors that helped you with the project.</p>
