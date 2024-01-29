from main.models import Skill


def add():
    from .models import suggestionSkills
    skills_list = [
    "Java", "Python", "C++", "JavaScript", "Ruby", "C#", "Swift", "Kotlin", "PHP", "TypeScript",
    "Go", "Rust", "Shell scripting", "HTML", "CSS", "React.js", "Angular", "Vue.js", "Node.js",
    "Django", "Flask", "Ruby on Rails", "ASP.NET", "SQL", "MySQL", "PostgreSQL", "MongoDB",
    "Redis", "Oracle Database", "Microsoft SQL Server", "SQLite", "Git", "Docker", "Kubernetes",
    "Jenkins", "Travis CI", "Ansible", "Terraform", "Vagrant", "Amazon Web Services (AWS)",
    "Microsoft Azure", "Google Cloud Platform (GCP)", "IBM Cloud", "Alibaba Cloud",
    "RESTful API Design", "GraphQL", "Serverless Architecture", "Microservices",
    "Spring Framework", "Express.js", "Responsive Web Design", "Web Accessibility (A11y)",
    "Progressive Web Apps (PWAs)", "Browser Developer Tools", "Cross-browser Compatibility",
    "Android Development (Kotlin/Java)", "iOS Development (Swift)", "Flutter",
    "React Native", "Xamarin", "Machine Learning Algorithms", "Neural Networks",
    "Natural Language Processing (NLP)", "Computer Vision", "TensorFlow", "PyTorch",
    "Scikit-Learn", "Data Analysis", "Data Visualization (e.g., Matplotlib, Seaborn)",
    "Statistical Analysis", "Pandas", "NumPy", "Jupyter Notebooks", "Network Security",
    "Ethical Hacking", "Cryptography", "Security Assessment and Testing",
    "SIEM (Security Information and Event Management)", "Linux/Unix", "Windows Server",
    "macOS", "Shell Scripting", "Agile Methodologies", "Scrum", "Kanban", "Jira", "Trello",
    "Git", "GitHub", "GitLab", "Bitbucket", "Microsoft Office Suite (Word, Excel, PowerPoint)",
    "Google Workspace (Docs, Sheets, Slides)", "Slack", "Microsoft Teams", "Zoom",
    "Data Structures", "Algorithmic Complexity", "Problem-solving Skills", "Code Optimization"]
    for skill_name in skills_list:
        SuggestionSkills.objects.create(skill=skill_name)