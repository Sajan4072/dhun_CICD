from django.test import TestCase
from django.test import TestCase
from predictor.models import Document
from django.test import Client
from django.urls import reverse
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
####unit tests

#ensures that the Document model works as expected when creating a new instance
# class DocumentModelTest(TestCase):
#     def test_document_creation(self):
#         document = Document.objects.create(name='Test Document', type='wav')
#         self.assertEqual(document.name, 'Test Document')
#         self.assertEqual(document.type, 'wav')



####white box tests
# def test_login_view_valid_credentials(self):
#     response = self.client.post(reverse('predictor:login_view'), {
#         'username': 'testuser',
#         'password': 'password'
#     })
#     self.assertEqual(response.status_code, 302)
#     self.assertRedirects(response, reverse('predictor:log'))





####black box tests

#ensure the index page loads correctly
class IndexViewTest(TestCase):
    def test_index_page_loads(self):
        client = Client()
        response = client.get(reverse('predictor:index'))
        self.assertEqual(response.status_code, 200)




##test to see if the nsures that the document upload functionality works as expected
# class DocumentUploadIntegrationTest(TestCase):
#     def test_document_upload(self):
#         file = SimpleUploadedFile("test.wav", b"file_content", content_type="audio/wav")
#         response = self.client.post(reverse('predictor:model_form_upload'), {'document': file})
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Genre Prediction")