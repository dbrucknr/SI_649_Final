    # class IndexView(TemplateView):
    # template_name = 'map_app/index.html'
    # def default_map(self, request):
    #     mapbox_access_token = 'pk.eyJ1IjoiZGJydWNrbnIiLCJhIjoiY2s4ajR1Nm44MGQzazNtcjBpcjYwcXVvMyJ9.mIDUxX2hIBZUT940zO2g3Q'
    #     return render(request, 'map_app/index.html', { 'mapbox_access_token': mapbox_access_token })
    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)

    #     x = [-2,0,4,6,7]
    #     y = [q**2-q+3 for q in x]
    #     trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': 10},
    #                         mode="lines",  name='1st Trace')

    #     data=go.Data([trace1])
    #     layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
    #     figure=go.Figure(data=data,layout=layout)
    #     div = opy.plot(figure, auto_open=False, output_type='div')

    #     context['graph'] = div

    #     return context

    # def get(self, request):

    #     filepath = '{REAL_PATH}/{CSV_PATH}'.format(
    #         REAL_PATH=os.path.dirname(os.path.realpath(__file__)),
    #         CSV_PATH='America_1.csv'
    #     )

    #     df_sample = pd.read_csv(filepath)
    #     df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
    #     df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
    #     df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']

    #     colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
    #                 "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
    #                 "#08519c","#0b4083","#08306b"]

    #     endpts = list(np.linspace(1, 12, len(colorscale) - 1))
    #     fips = df_sample['FIPS'].tolist()
    #     values = df_sample['Unemployment Rate (%)'].tolist()

    #     fig = ff.create_choropleth(
    #         fips=fips, values=values,
    #         binning_endpoints=endpts,
    #         colorscale=colorscale,
    #         show_state_data=False,
    #         show_hover=True, centroid_marker={'opacity': 0},
    #         asp=2.9, title='USA by Unemployment %',
    #         legend_title='% unemployed'
    #     )

    #     fig.layout.template = None
        # fig.show()

        # return render(request, 'map_app/index.html', context = {'fig': fig})