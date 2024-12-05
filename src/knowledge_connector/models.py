from django.db import models


class KC_Submission(models.Model):
    EDITORIAL_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("in_progress", "In Progress"),
    ]

    id = models.AutoField(primary_key=True)
    submission_type = models.CharField(max_length=50, null=True, blank=True)

    # Article-specific fields
    title = models.CharField(max_length=255)
    authors = models.TextField()
    abstract = models.TextField()
    keywords = models.TextField()

    # Journal-specific fields
    journal_name = models.CharField(max_length=255, null=True, blank=True)
    volume_issue_number = models.CharField(max_length=100, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    doi = models.CharField(max_length=255, null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)

    # Metadata fields
    upload_date = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=255, null=True, blank=True)
    cover_image = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    # User relationship
    user = models.ForeignKey(
        "core.Account", on_delete=models.CASCADE, related_name="article_submissions"
    )

    # Status and tracking
    status = models.CharField(max_length=50, default="pending")
    editorial_status = models.CharField(
        max_length=20, choices=EDITORIAL_STATUS_CHOICES, null=True, blank=True
    )
    views = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)

    # Timestamps
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Article Submissions"
        db_table = "submissions"

    def __str__(self):
        return self.title or f"Article Submission {self.id}"
