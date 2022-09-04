require 'rails_helper'

RSpec.describe "Sessions", type: :request do
  describe "GET /new" do
    it "returns http success" do
      get login_path
      expect(response).to have_http_status :success
    end
  end

  describe 'DELETE /logout' do
    it 'ログアウトができること' do
      user = FactoryBot.create(:user)
      post login_path, params: { session: { email: user.email,
                                            password: user.password } }
      expect(logged_in?).to be_truthy

      delete logout_path
      expect(logged_in?).to_not be_truthy
    end
  end
end
