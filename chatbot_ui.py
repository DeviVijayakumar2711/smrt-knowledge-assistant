import gradio as gr

# Placeholder function for AI responses
def chatbot(query, uploaded_files):
    if uploaded_files:
        file_names = uploaded_files.name if isinstance(uploaded_files, list) else uploaded_files.name
    else:
        file_names = "No files uploaded."
    
    return f"📝 AI response for: {query}\n\n📂 Files: {file_names}"

# UI Layout
with gr.Blocks(css="body {font-family: Arial, sans-serif;}") as demo:
    
    # Header Section
    gr.Markdown("# 🧠 SMRT Knowledge Assistant")
    gr.Markdown("**Your AI-powered research assistant to organize, analyze, and chat with your knowledge sources.**")

    with gr.Row():
        
        # Left Sidebar - File Upload & Sources
        with gr.Column(scale=2):
            gr.Markdown("## 📂 Upload & Select Sources")
            file_upload = gr.File(label="Upload Your Documents", interactive=True, file_types=[".txt", ".pdf", ".png", ".jpg", ".mp3", ".mp4"])
            
            gr.Markdown("### 📌 Select Knowledge Sources")
            source_buttons = [
                gr.Checkbox(label="📖 Getting Started Guide", value=True),
                gr.Checkbox(label="⚙️ SMRT Assistant Features", value=True),
                gr.Checkbox(label="🗂️ Knowledge Glossary", value=True),
                gr.Checkbox(label="❓ Troubleshooting & FAQ", value=True),
            ]

            gr.Markdown("## 🎬 How to Use This UI?")
            gr.Markdown("""
            - **Upload documents**: PDFs, text files, images, and audio.
            - **Select sources**: Enable the knowledge sources relevant to your query.
            - **Ask questions**: Chat with the AI in the middle section.
            - **Save responses**: Store important responses in notes below.
            """)

        # Middle Section - Chat Interface
        with gr.Column(scale=6):
            gr.Markdown("## 💬 Chat with SMRT Assistant")
            gr.Markdown("Type a question below to interact with your knowledge sources.")
            user_query = gr.Textbox(label="Ask something...", placeholder="Type your question here...")
            chat_output = gr.Textbox(label="AI Response", interactive=False, lines=5)
            
            with gr.Row():
                chat_button = gr.Button("🚀 Send", size="md")
                clear_chat_button = gr.Button("🔄 Clear Chat", size="md")

            # Notes section below Chat
            gr.Markdown("## 📝 Notes & Actions")
            notes = gr.Textbox(label="Save your notes here", interactive=True, lines=4)
            with gr.Row():
                study_guide_btn = gr.Button("📚 Study Guide", size="md")
                briefing_doc_btn = gr.Button("📝 Briefing Doc", size="md")
            with gr.Row():
                faq_btn = gr.Button("💡 FAQ", size="md")
                timeline_btn = gr.Button("📆 Timeline", size="md")
            with gr.Row():
                export_notes_button = gr.Button("📥 Export Notes", size="md")
                settings_button = gr.Button("⚙️ Settings", size="md")

    # Chat Functionality
    chat_button.click(fn=chatbot, inputs=[user_query, file_upload], outputs=chat_output)
    clear_chat_button.click(fn=lambda: "", inputs=[], outputs=[chat_output, user_query])

# Run UI with Public Link
demo.launch(share=True, debug=True)
