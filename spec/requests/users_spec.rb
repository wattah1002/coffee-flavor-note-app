require 'rails_helper'

RSpec.describe "Users", type: :request do
  describe "GET /new" do
    it "returns http success" do
      # get "/signup"
      get signup_path
      expect(response).to have_http_status(:success)
    end

    it "タイトルに Sign up が含まれること" do
      get signup_path
      expect(response.body).to include "Sign up"
    end
  end
end
