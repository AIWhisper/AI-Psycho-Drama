class SessionManager:
    def __init__(self):
        self.active_sessions = {}
        
    def create_session(self, session_id):
        self.active_sessions[session_id] = {
            "status": "initialized",
            "safety_active": True
        }
