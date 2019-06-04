.PHONY: all
all: data_downloading modeling clean

# download data from a public S3 bucket
data_downloading:
	python src/download_data.py

# (optional, not included in 'make all') uploading downloaded data to designated private S3 bucket
data_uploading:
	python src/upload_data.py --input_file_path "data/red.csv" --bucket_name "yzhu-project" --output_file_path "red3.csv"

# run all modeling steps
modeling:
	python src/evaluate_model.py

# Clean up things
clean:
	rm -rf .pytest_cache


