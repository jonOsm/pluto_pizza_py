from db.seed.user_factory import UserFactory

if __name__ == "__main__":
    print("Seeding DB...")
    UserFactory.create()
