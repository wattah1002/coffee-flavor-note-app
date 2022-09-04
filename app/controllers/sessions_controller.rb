class SessionsController < ApplicationController
  def new
  end

  def create
    user = User.find_by(email: params[:session][:email].downcase)
    if user && user.authenticate(params[:session][:password])
      # redirect to user page
    else
      flash.now[:danger] = '無効なメールアドレスまたはパスワードです．'
      render 'new'
    end
  end

  def destroy
  end
end
