from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["POST"])
def upload_pdf(request):
    if "pdf" in request.FILES:
        pdf_file = request.FILES["pdf"]
        print(pdf_file, flush=True)
        # Process or save pdf_file as needed
        # ...

        return Response(
            {"message": "PDF uploaded successfully!"}, status=status.HTTP_201_CREATED
        )
    else:
        return Response(
            {"message": "No PDF file found in request"},
            status=status.HTTP_400_BAD_REQUEST,
        )
