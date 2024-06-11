from flask import Blueprint, jsonify, request

review_routes = Blueprint('review_routes', __name__)

# Dummy data for demonstration
example_reviews = [
    {
        "id": 1,
        "place_id": 1,
        "user_id": 1,
        "rating": 4,
        "comment": "Great place to stay!",
        "created_at": "2024-06-15T12:00:00Z",
        "updated_at": "2024-06-15T12:00:00Z"
    },
    {
        "id": 2,
        "place_id": 1,
        "user_id": 2,
        "rating": 5,
        "comment": "Awesome experience!",
        "created_at": "2024-06-16T12:00:00Z",
        "updated_at": "2024-06-16T12:00:00Z"
    }
]

@review_routes.route('/places/<int:place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.json
    user_id = data.get('user_id')
    rating = data.get('rating')
    comment = data.get('comment')

    # Validate user_id and place_id (dummy validation)
    if place_id not in [1, 2, 3]:
        return jsonify({"error": "Place not found"}), 404
    if user_id not in [1, 2]:
        return jsonify({"error": "User not found"}), 404

    # Check if user is the host of the place (dummy logic)
    if user_id == 1:
        return jsonify({"error": "Host cannot review their own place"}), 400

    # Validate rating
    if rating not in [1, 2, 3, 4, 5]:
        return jsonify({"error": "Invalid rating"}), 400

    # Create the review (dummy creation)
    new_review = {
        "id": len(example_reviews) + 1,
        "place_id": place_id,
        "user_id": user_id,
        "rating": rating,
        "comment": comment,
        "created_at": "2024-06-17T12:00:00Z",
        "updated_at": "2024-06-17T12:00:00Z"
    }
    example_reviews.append(new_review)
    return jsonify(new_review), 201

@review_routes.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = next((review for review in example_reviews if review["id"] == review_id), None)
    if review:
        return jsonify(review), 200
    else:
        return jsonify({"error": "Review not found"}), 404

@review_routes.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    review = next((review for review in example_reviews if review["id"] == review_id), None)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    # Implement update logic here (dummy logic)
    review.update(data)
    return jsonify(review), 200

@review_routes.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    global example_reviews
    example_reviews = [review for review in example_reviews if review["id"] != review_id]
    return jsonify({}), 204

