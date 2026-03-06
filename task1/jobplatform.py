class JobPlatform:
    def __init__(self):
        self.users = []
        self.jobs = []
        self.applications =[]
        self.current_user = None
        self.next_user_id = 1
        self.next_job_id = 1
        self.next_application_id = 1

    def register(self, name, email, password, user_type):
        for user in self.users:
            if user['email'] == email:
                print ("This email is registered.")
                return False
        #todo 后面缝合代码的时候会改  
        new_user = {
            'user_id' : self.next_user_id,
            'name' : name,
            'email' : email,
            'password' : password,
            'user_type' : user_type}    
        self.users.append(new_user)
        self.next_user_id += 1

    def login(self, email, password):
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                self.current_user = user
                return True
        print("password or email is incorrect.")
        return False
        
    def logout(self):
        self.current_user = None
        print("logout successful.")
    
    def search_job(self, keyword):
        result = []
        for job in self.jobs:
            if keyword.lower() in job['title'].lower() or keyword.lower() in job['company'].lower():
                result.append(job)
        return result
        
    def check_job_detail(self, job_id):
        for job in self.jobs:
            if job['job_id'] == job_id:
                return job
        return None
        
    def apply_job(self, job_id, resume_id):
        if not self.current_user:
            print("please login.")
            return None
        job = self.check_job_detail(job_id)
        if not job:
            return
        
        #todo

        from jobapplication import JobApplication
        application = JobApplication(
            self.next_application_id,
            job,
            self.current_user,
            None
        )
        self.applications.append(application)
        self.next_application_id +=1
        print(f"Submitted successfully. ID{application.application_id}")
        return application
    
    def get_my_applications(self):
        if not self.current_user:
            print("Please login first.")
            return []
    
        my_apps = []
        for app in self.applications:
            if app.applicant['user_id'] == self.current_user['user_id']:
                my_apps.append(app)
        return my_apps
    
#---------------------------------------------------------
    def post_job(self, title, description, company):
        if not self.current_user:
            print("pleace login.")
            return None
        #todo
        job = {
            'job_id': self.next_job_id,
            'title' : title,
            'company' : company,
            'description' : description
        }
        self.jobs.append(job)
        self.next_job_id +=1
        print("successfully.")
        return True
    
    def view_applicant(self, job_id):
        applicant = []
        for application in self.applications:
            if application.job['job_id'] == job_id:
                applicant.append(application)
        return applicant
        

