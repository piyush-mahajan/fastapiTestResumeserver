from fastapi import FastAPI
from rich.console import Console
from rich.table import Table
from rich.text import Text

app = FastAPI()
console = Console()

resume_data = {
    "name": "Piyush Mahajan",
    "contact": {
        "email": "piyushmahajan1704@gmail.com",
        "phone": "+91 8669760171",
        "linkedin": "linkedin.com/in/piyush-mahajan"
    },
    "summary": "Built 5+ React.js apps | 4+ Full Stack apps | 2+ Mobile Apps | 3+ ML Apps",
    "internships": [
         {
            "title": "Developer and AI Innovation Intern",
            "company": "Tangible IT Mexico",
            "duration": "November 2024 - December 2024",
            "location": "Remote",
            "description": "Developed an AI-powered summarization product using Azure AI services, React.js, and Python, designed to simplify student workflows and enhance the AI ecosystem with scalable solutions."
        },
         {
            "title": "Full Stack Development Intern",
            "company": "Klaimify Private Limited",
            "duration": "September 2024 - October 2024",
            "location": "Remote",
            "description": "Built and optimized React.js and Next.js dashboards, enhancing UX, scalability, and API integration for seamless product performance, delivering an intuitive user experience for core product features."
        },
        {
            "title": "Web Development Intern",
            "company": "Concoder Services",
            "duration": "August 2023 - September 2023",
            "location": "Remote",
            "description": "Built full-stack web applications with React.js, Next.js, Node.js, and MongoDB, improving performance, scalability, and team delivery by 20% through effective collaboration and design tools like Figma and Adobe Photoshop."
        },
        {
            "title": "Contributor",
            "company": "Hack2skill, GirlScript, Timechain Labs",
            "duration": "June 2023",
            "location": "Remote",
            "description": "Led campus ambassador efforts for GirlScript, promoting the GirlScript Summer of Code and contributing to blockchain projects with Ethereum and Solidity. Participated in TimeChain, India’s first open-source blockchain program."
        },
       
       
    ],
    "projects": [
        {
            "title": "AI SaaS Platform",
            "description": "Engineered an AI image SaaS platform for image restoration, recoloring, object removal, and generative fill. Integrated secure payment processing with Stripe and implemented robust user authentication using Clerk. Enabled advanced search and community image showcase.",
            "technologies": ["Next.js", "TypeScript", "MongoDB", "Cloudinary"]
        },
        {
            "title": "Figma Clone",
            "description": "Developed a real-time collaborative tool with multi-cursor support, chat functionality, and design element management, enabling seamless team design collaboration.",
            "technologies": ["Next.js", "TypeScript", "Liveblocks", "Fabric.js"]
        },
        {
            "title": "MahaGPT",
            "description": "Created an interactive AI tool with capabilities like system health checks, PDF and image interaction, and a YouTube summarizer, streamlining user interaction and content accessibility.",
            "technologies": ["Python", "Streamlit", "GeminiAI"]
        },
        {
            "title": "Text Summarizer",
            "description": "Implemented advanced algorithms and models to analyze and summarize textual content in a human-like manner, minifying lengthy articles or documents.",
            "technologies": ["React.js", "RESTful API", "Node.js"]
        }
    ],
    "achievements": [
        "Microsoft Learn Student Ambassador",
        "Google DSC’s Web and UI/UX Head",
        "300 Days Badge 2024, 2023 & 2022 on LeetCode",
        "1st Institution Rank on GeeksForGeeks",
        "Postman Student Expert",
        "Passed LinkedIn Assessment for JavaScript and React.js"
    ]
}

# @app.get("/")
# def get_resume():
#     return resume_data

@app.get("/")
def get_pretty_resume():
    console.print(Text("Piyush Mahajan", style="bold magenta"))
    console.print(Text("Contact:", style="bold yellow"))
    console.print(f"📧 Email: [blue]{resume_data['contact']['email']}[/blue]")
    console.print(f"📞 Phone: [green]{resume_data['contact']['phone']}[/green]")
    console.print(f"🔗 LinkedIn: [cyan]{resume_data['contact']['linkedin']}[/cyan]\n")
    
    table = Table(title="Internships", style="bold red")
    table.add_column("Title", style="bold white")
    table.add_column("Company", style="yellow")
    table.add_column("Duration", style="cyan")
    for internship in resume_data["internships"]:
        table.add_row(internship["title"], internship["company"], internship["duration"])
    console.print(table)
    
    table = Table(title="Projects", style="bold blue")
    table.add_column("Project Name", style="bold white")
    table.add_column("Technologies", style="yellow")
    for project in resume_data["projects"]:
        tech_list = ", ".join(project["technologies"])
        table.add_row(project["title"], tech_list)
    console.print(table)
    
    console.print(Text("Achievements:", style="bold green"))
    for achievement in resume_data["achievements"]:
        console.print(f"✔ {achievement}", style="white")
    return resume_data
