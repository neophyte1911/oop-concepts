'''
"YAGNI" stands for "You Aren't Gonna Need It". It is a principle in software development that suggests developers should only implement features that are necessary for the current requirements and not add any additional functionality that might be needed in the future. This principle is based on the idea that adding unnecessary features can lead to increased complexity, longer development times, and potentially more bugs.

The YAGNI principle is closely related to the "KISS" principle ("Keep It Simple, Stupid"), which advocates for simplicity in design and avoiding unnecessary complexity. Both principles encourage developers to focus on delivering the simplest solution that meets current requirements, rather than trying to anticipate and accommodate potential future needs.
'''


# ❌ YAGNI violation: extra method nobody uses yet
class Report:
    def generate_pdf(self): ...
    def generate_excel(self): ...
    def generate_html(self): ...
    def generate_markdown(self): ...
    # user only ever needs HTML today

# ✅ YAGNI: implement only what’s required
class Report:
    def generate_html(self): ...
