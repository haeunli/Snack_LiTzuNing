ef
update_snack(request, id):
snack = Snack.objects.get(id=id)
form = SnackForm(request.POST or None, instance=snack)

if form.is_valid():
    form.save()
    return redirect('list_snack')

return render(request, 'usermgmt/snack_form.html', {'form': form, 'snack': snack})
