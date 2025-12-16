def load_styles():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    :root {
        --accent: #6366f1;
        --accent2: #22d3ee;
        --muted: #6b7280;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Background gradient */
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(99,102,241,0.18), transparent 40%),
            radial-gradient(circle at bottom right, rgba(34,211,238,0.18), transparent 40%);
    }

    /* Remove Streamlit clutter */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* Hero */
    .hero {
        text-align: center;
        margin: 3rem 0 2rem;
    }

    .hero h1 {
        font-size: 3rem;
        font-weight: 700;
        letter-spacing: -1px;
    }

    .hero p {
        margin-top: 0.5rem;
        color: var(--muted);
    }

    /* Inputs */
    input {
        border-radius: 14px !important;
        padding: 14px !important;
    }

    /* Buttons */
    button[kind="primary"] {
        background: linear-gradient(135deg, var(--accent), var(--accent2));
        border-radius: 16px;
        font-weight: 600;
        color: white;
        padding: 14px;
    }

    /* Result */
    .result {
        margin-top: 18px;
        padding: 14px 16px;
        border-radius: 14px;
        background: linear-gradient(
            135deg,
            rgba(99,102,241,0.12),
            rgba(34,211,238,0.12)
        );
        font-weight: 600;
        word-break: break-all;
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        font-weight: 600;
        opacity: 0.6;
    }

    button[aria-selected="true"] {
        opacity: 1;
    }
    </style>
    """
